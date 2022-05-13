import inspect
import os
import sys
import threading
from logging import raiseExceptions
from pathlib import Path
from urllib.parse import urlparse

from git import Repo
from icecream import ic

from .file_management import create_directory, download_file, is_archive, uncompress


def download_model(
    url: str,
    output_path: str,
    uncompress_after_download=True,
    file_type=None,
    reset=True,
    branch="origin",
) -> str:
    """download a model and uncompress it if necessary
    reset lets you decide not to force sync between huggingface hub and you local repo (for testing purposes for instance)
    """
    
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    model_root_path = os.path.dirname(os.path.join(cwd, rel_path))

    # check env to see if mutualized_storage had been set
    mutualized_storage = os.getenv('MODEL_MUTUALIZED_STORAGE', True)
    mutualized_storage_root = os.getenv('MODEL_MUTUALIZED_STORAGE_ROOT', '/tmp/gladia/models/')

    if not os.path.isabs(output_path):
        if mutualized_storage == True :
            output_path = os.path.join(mutualized_storage_root, rel_path, output_path)
        else:
            output_path = os.path.join(model_root_path, output_path)

    ic("Downloading model", url, output_path)

    url_domain = urlparse(url).netloc

    if url_domain == "huggingface.co" or url_domain == "www.huggingface.co":
        # check if directory exists if not clone it
        # else pull
        os.environ["GIT_LFS_SKIP_SMUDGE"] = "1"
        if not os.path.isdir(Path(output_path)):
            ic("Cloning HuggingFace Model", url)
            Repo.clone_from(url, output_path)
            os.system(f"cd {output_path} && git lfs pull")
        else:
            if reset:
                ic("Pulling HuggingFace Model", url)
                repo = Repo(output_path)
                repo.git.reset("--hard", "origin/main")
                os.system(f"cd {output_path} && git lfs pull")
    else:
        ic("Downloading", url)
        download_file(url, output_path)

        if is_archive(output_path) and uncompress_after_download:
            ic("Uncompressing", output_path)
            uncompress(output_path)

    return output_path


def download_models(model_list: dict) -> dict:
    """model_list should be [(url, output_path, uncompression_mode)]"""

    # manage relative imports
    namespace = sys._getframe(1).f_globals
    cwd = os.getcwd()
    rel_path = namespace["__file__"]
    rel_path = rel_path.lstrip('./')
    if ".py" in rel_path:
        rel_path = os.path.dirname(rel_path)

    # used in case of relative path
    model_root_path = os.path.dirname(os.path.join(cwd, rel_path))

    ic("Downloading multiple models")
    threads = []
    output = dict()

    # check env to see if mutualized_storage had been set
    mutualized_storage = os.getenv('MODEL_MUTUALIZED_STORAGE', True)
    mutualized_storage_root = os.getenv('MODEL_MUTUALIZED_STORAGE_ROOT', '/tmp/gladia/models/')

    for key, model in model_list.items():
        if not os.path.isabs(model["output_path"]):
            if mutualized_storage:
                model["output_path"] = os.path.join(mutualized_storage_root, rel_path,  model["output_path"])
            else:
                model["output_path"] = os.path.join(model_root_path, model["output_path"])

            t = threading.Thread(
                target=download_model,
                args=(
                    model["url"],
                    model["output_path"],
                ),
            )
            output[key] = model
            threads.append(t)
            t.start()

    return output
