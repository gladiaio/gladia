import os
import re
import sys
import forge
import asyncio
import pathlib
import inflect
import tempfile
import warnings
import starlette
import importlib
from icecream import ic
from shlex import quote
import json

from pathlib import Path
from .casting import cast_response
from pydantic import create_model
from .file_management import write_tmp_file
from importlib.machinery import SourceFileLoader
from fastapi import APIRouter, File, Query, UploadFile, HTTPException, status

versions = list()
available_versions = list()

PATTERN = re.compile(r'((\w:)|(\.))((/(?!/)(?!/)|\\{2})[^\n?"|></\\:*]+)+')

def is_binary_file(file_path: str) -> bool:
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

    return is_binary_string(open(file_path, 'rb').read(1024))


def is_valid_path(string: str):
    if string and isinstance(string, str) and PATTERN.match(string):
        return True
    else:
        return False


def singularize(word):
    if inflect.engine().singular_noun(word):
        if word == "apis/text/text/sentiment-analyses":
            return "apis/text/text/sentiment-analysis"
        else:
            return inflect.engine().singular_noun(word)
    else:
        return word


def pluralize(word):
    if inflect.engine().plural_noun(word):
        return inflect.engine().plural_noun(word)
    else:
        return word


def dict_model(name: str, dict_def: dict):
    fields = {}

    for field_name, value in dict_def.items():
        if isinstance(value, tuple):
            fields[field_name] = value
        elif isinstance(value, dict):
            fields[field_name] = (dict_model(f"{name}_{field_name}", value), ...)
        else:
            raise ValueError(f"Field {field_name}:{value} has invalid syntax")

    return create_model(name, **fields)


def get_module_infos(root_path=None) -> list:
    if root_path:
        caller_file = root_path
    else:
        caller_file = sys._getframe(1).f_globals["__file__"]

    pwd = str(pathlib.Path(caller_file).absolute()).split("/")

    plugin = pwd[len(pwd) - 3: len(pwd)]
    tags = ".".join(plugin)[:-3]
    task = plugin[-1][:-3]

    return task, plugin, tags


def versions_list(root_path=None) -> list:
    # used for relative paths
    if root_path:
        rel_path = root_path
    else:
        namespace = sys._getframe(1).f_globals

        cwd = os.getcwd()

        rel_path = namespace["__file__"]
        rel_path = os.path.join(cwd, rel_path)

    sub_dir_to_crawl = f"{os.path.splitext(os.path.basename(rel_path))[0]}"
    sub_dir_to_crawl = pluralize(sub_dir_to_crawl)

    versions = list()
    package_path = str(Path(rel_path).parent.joinpath(sub_dir_to_crawl))

    # package = SourceFileLoader(sub_dir_to_crawl, package_path).load_module()

    for fname in os.listdir(package_path):
        if os.path.isdir(os.path.join(package_path, fname)):
            if pathlib.Path(os.path.join(package_path, fname, "__init__.py")).exists():
                versions.append(fname)

    return versions, package_path


class TaskRouter:
    def __init__(self, router: APIRouter, input, output, default_model: str):
        self.input = input
        self.output = output
        self.default_model = default_model

        namespace = sys._getframe(1).f_globals

        # concate the package name (i.e apis.text.text) with the model filename (i.e word-alignment.py) to obtain the relative path
        rel_path = os.path.join(namespace["__package__"].replace(".", "/"), namespace["__file__"].split("/")[-1])


        self.task, self.plugin, self.tags = get_module_infos(root_path=rel_path)
        self.versions, self.root_package_path = versions_list(rel_path)

        if not self.__check_if_model_exist(self.root_package_path, default_model):
            return

        input_list = list()

        if isinstance(input, str):
            if input in ["image", "video", "sound"]:
                input_list.append(forge.arg(input, type=UploadFile, default=File(...)))
            elif input == "text":
                input_list.append(forge.arg("text", type=str, default="default Text"))
            elif input == "list":
                input_list.append(forge.arg("list", type=list), default=list())
            elif input == "dict":
                input_list.append(forge.arg("dict", type=dict), default=dict())

        elif isinstance(input, list):
            for item in input:
                if item["type"] in ["text", "str", "string"]:
                    item["type"] = str
                elif item["type"] in ["number", "int", "integer"]:
                    item["type"] = int
                elif item["type"] in ["float", "decimal"]:
                    item["type"] = float

                if item["type"] in ["image", "sound", "video"]:
                    input_list.append(
                        forge.arg(item["name"], type=UploadFile, default=File(...))
                    )
                else:
                    input_list.append(
                        forge.arg(
                            item["name"], type=item["type"], default=item["default"]
                        )
                    )

        input_list.append(
            forge.arg(
                "model", type=str, default=Query(self.default_model, enum=self.versions)
            )
        )

        @router.get(
            "/",
            summary=f"Get list of models available for {self.task}",
            tags=[self.tags],
        )
        async def get_versions():
            return self.versions

        @router.post(
            "/",
            summary=f"Apply model for the {self.task} task for a given models",
            tags=[self.tags],
            #            response_model=self.output
        )
        @forge.sign(*input_list)
        async def apply(*args, **kwargs):

            for key, value in kwargs.items():
                if isinstance(value, starlette.datastructures.UploadFile):
                    # make all io to files ?
                    kwargs[key] = await value.read()

            model = kwargs["model"]
            del kwargs["model"]

            module_path = f"{self.root_package_path}/{model}/"

            if not os.path.exists(module_path):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Model {model} does not exist"
                )

            # if a virtualenv
            if os.path.isfile(os.path.join(module_path, 'env.yaml')):
                if not os.path.isdir(os.path.join(module_path, '.venv')):
                    # FIXME: this is not working
                    os.system("python3 /app/venv-builder/setup_custom_envs.py -l -p 1 -r " + module_path)

                routeur = singularize(self.root_package_path)

                this_routeur = importlib.import_module(routeur.replace('/', '.'))

                output = this_routeur.output

                inputs = this_routeur.inputs

                # convert io Bytes to files
                # input_files to clean
                input_files = list()
                for input in inputs:
                    if input["type"] in ["image", "sound", "video"]:
                        tmp_file = write_tmp_file(kwargs[input["name"]])
                        kwargs[input["name"]] = tmp_file
                        input_files.append(tmp_file)

                    elif input["type"] in ["text"]:
                        kwargs[input["name"]] = quote(kwargs[input["name"]])

                output_tmp_result = tempfile.NamedTemporaryFile().name
                sync = False
                kwargs_str = json.dumps(kwargs).replace('"', '\\"')

                model = quote(model)
                output_tmp_result = quote(output_tmp_result)

                # check https://www.dev2qa.com/how-to-import-a-python-module-from-a-python-file-full-path/
                # for a better solution

                cmd = f"""LD_LIBRARY_PATH=/usr/local/nvidia/lib64:/usr/local/cuda/lib64:/opt/conda/lib; cd /app/{module_path} && \
pipenv run python3 -c "
import os
os.environ['LD_LIBRARY_PATH'] = '/usr/local/nvidia/lib64:/usr/local/cuda/lib64:/opt/conda/lib'
from PIL import Image
import importlib.util
spec = importlib.util.spec_from_file_location('/app/{module_path}', '/app/{module_path}/{model}.py')
this_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(this_module)
output = this_module.predict(**{kwargs_str})

#FIXME
## convert output to bytes
## move this to string comparison
if isinstance(output, Image.Image):
    output.save('{output_tmp_result}', format='PNG')
else:
    with open('{output_tmp_result}', 'w') as f:
        f.write(str(output))
" """
                
                proc = await asyncio.create_subprocess_shell(
                    cmd,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE,
                    start_new_session=True)

                stdout, stderr = await proc.communicate()

                print()
                print(stderr)
                print()
                
                if is_binary_file(output_tmp_result):
                    file = open(output_tmp_result, "rb")
                    result = file.read()
                    file.close()
                else:
                    file = open(output_tmp_result, "r")
                    result = file.read()
                    file.close()    
                

                os.system(f"rm {output_tmp_result}")

                for input_file in input_files:
                    os.system(f"rm {input_file}")

            else:
                this_module = importlib.machinery.SourceFileLoader(
                    model, f"{self.root_package_path}/{model}/{model}.py"
                ).load_module()

                result = getattr(this_module, f"predict")(*args, **kwargs)
            try:
                return cast_response(result, self.output)
            except Exception as e:
                print(e)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"The following error occurred: {str(e)}"
                )
            finally:
                if isinstance(result, str):
                    try:
                        if result != "/" and is_valid_path(result) and os.path.exists(result):
                            os.system(f"rm {result}")
                    except:
                        pass

    def __check_if_model_exist(self, root_package_path: str, default_model: str) -> bool:
        """
        Verify that the default model for the task is implemented.

        :param root_package_path: path to the package
        :param default_model: name of the default model for the task
        :return: True if it exists, False otherwise.
        """

        model_dir = os.path.join(root_package_path, default_model)
        model_file = os.path.join(root_package_path, default_model, f"{default_model}.py")

        if not os.path.exists(root_package_path):
            warnings.warn(f"task dir ({root_package_path}) does not exist, skipping {self.task}")
            return False

        elif not os.path.exists(model_dir):
            warnings.warn(f"model_dir ({model_dir}) does not exist, skipping {self.task}")
            return False

        elif not os.path.exists(model_file):
            warnings.warn(f"model_file ({model_file}) does not exist, skipping {self.task}")
            return False

        return True
