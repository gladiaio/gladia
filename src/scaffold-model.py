import os
from importlib.machinery import SourceFileLoader
from pathlib import Path
from pprint import pprint

import easyargs
import inflect
import inquirer
from inquirer.themes import GreenPassion

p = inflect.engine()


def task_exists(input_type, output_type, task_name):
    input_type = input_type.lower()
    output_type = output_type.lower()
    task_name = task_name.lower()

    if p.singular_noun(task_name) != False:
        task_name = p.singular_noun(task_name)

    task_routeur_path = os.path.join("apis", input_type, output_type, f"{task_name}.py")
    task_path = os.path.join("apis", input_type, output_type, p.plural(task_name))

    output = True

    if not os.path.exists(task_routeur_path):
        print(f"Missing {task_routeur_path} ; I will build it for you")
        output = False

    if not os.path.exists(task_path):
        print(f"Missing {task_path} ; I will build it for you")
        output = False

    return output


def model_exists(input_type, output_type, task_name, model_name):
    input_type = input_type.lower()
    output_type = output_type.lower()
    task_name = task_name.lower()

    if p.singular_noun(task_name) != False:
        task_name = p.singular_noun(task_name)

    model_name = model_name.lower()
    task_path = os.path.join("apis", input_type, output_type, p.plural(task_name))
    model_path = os.path.join(task_path, f"{model_name}")

    output = True
    if not Path(model_path).exists():
        print(f"Missing {model_path} ; I will build it for you")
        output = False

    if not Path(os.path.join(model_path, "__init__.py")).exists():
        print(
            f"Missing {os.path.join(model_path, '__init__.py')} ; I will build it for you"
        )
        output = False

    if not Path(os.path.join(model_path, f"{model_name}.py")).exists():
        print(
            f"Missing {os.path.join(model_path, f'{model_name}.py')} ; I will build it for you"
        )
        output = False

    return output


def create_task_routeur(
    input_type, output_type, task_name, inputs, output, model_name="default_model"
):
    input_type = input_type.lower()
    output_type = output_type.lower()
    task_name = task_name.lower()

    if p.singular_noun(task_name) != False:
        task_name = p.singular_noun(task_name)

    task_routeur_path = os.path.join("apis", input_type, output_type, f"{task_name}.py")
    task_path = os.path.join("apis", input_type, output_type, p.plural(task_name))
    model_name = model_name.lower()

    if not os.path.exists(task_path):
        Path(task_path).mkdir(parents=True, exist_ok=True)

    with open(task_routeur_path, "w") as f:
        f.write(
            f"""from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()"""
        )

        f.write(
            """
inputs = ["""
        )
        for input in inputs:
            f.write(
                """
    {
        'name': '"""
                + input["input_name"]
                + """',
        'type': '"""
                + input["input_type"]
                + """',
        'default': '"""
                + input["default_value"]
                + """',
        'placeholder': '"""
                + input["placeholder"]
                + """',
        'tooltip': '"""
                + input["tooltip"]
                + """'
    },
"""
            )
        f.write(
            """]
        """
        )

        f.write(
            """
output = {
        'name': '"""
            + output["output_name"]
            + """',
        'type': '"""
            + output["output_type"]
            + """',
        'example': '"""
            + output["example_value"]
            + """'
    }

        """
        )

        f.write(
            f"""
TaskRouter(router=router, input=inputs, output=output, default_model="{model_name}")
"""
        )

    return task_routeur_path


def create_model(input_type, output_type, task_name, model_name, inputs, output):
    input_type = input_type.lower()
    output_type = output_type.lower()
    task_name = task_name.lower()

    if p.singular_noun(task_name) != False:
        task_name = p.singular_noun(task_name)

    model_name = model_name.lower()

    task_routeur_path = os.path.join("apis", input_type, output_type, f"{task_name}.py")
    task_path = os.path.join("apis", input_type, output_type, p.plural(task_name))

    model_path = os.path.join(task_path, model_name)

    if not os.path.isdir(model_path):
        Path(model_path).mkdir(parents=True, exist_ok=True)

    if not os.path.isfile(os.path.join(model_path, "__init__.py")):
        Path(os.path.join(model_path, "__init__.py")).touch()

    if len(inputs) == 0:
        task_routeur = SourceFileLoader(
            "this_task_routeur", task_routeur_path
        ).load_module()

        task_routeur_inputs = task_routeur.inputs
        inputs = []
        for input in task_routeur_inputs:
            inputs.append({"input_name": input["name"]})

    with open(os.path.join(model_path, f"{model_name}.py"), "w") as f:
        f.write(
            f"""
#your imports here
import os, sys

"""
        )
        input_params = ""

        for param in inputs:
            input_params += f"{param['input_name']}, "

        input_params = input_params[:-2]

        f.write(
            f"""
# mandatory predict function
def predict({input_params}):
    #your code here
    return output
"""
        )
    return os.path.join(model_path, f"{model_name}.py")


def scaffold_task():

    set_main_input = [
        inquirer.List(
            "main_input_type",
            message="What is the main input type ?",
            choices=["image", "text", "sound", "video"],
            default="image",
        )
    ]

    input_type = inquirer.prompt(set_main_input, theme=GreenPassion())[
        "main_input_type"
    ]

    set_main_output = [
        inquirer.List(
            "main_output_type",
            message="What is the main output type ?",
            choices=["image", "text", "sound", "video"],
            default="image",
        )
    ]

    output_type = inquirer.prompt(set_main_output, theme=GreenPassion())[
        "main_output_type"
    ]

    set_task_name = [
        inquirer.Text(
            "task_name",
            message="What is the task name ?",
            default="task_name_no_space_dash_only"
            # validate=lambda x: x != ""
        )
    ]

    task_name = inquirer.prompt(set_task_name, theme=GreenPassion())[
        "task_name"
    ].lower()

    set_input = [
        inquirer.List(
            "input_type",
            message="Set input",
            choices=["image", "text", "sound", "video"],
            default="image",
        ),
        inquirer.Text(
            "input_name",
            message="Input name for the new {input_type}",
            default="{input_type}"
            #            validate=lambda x: x != ""
        ),
        inquirer.Text(
            "default_value",
            message="Default Value for the new {input_type}",
            default="{input_type}"
            #            validate=lambda x: x != ""
        ),
        inquirer.Text(
            "placeholder",
            message="Placeholder for the new {input_type}",
            default="{default_value}"
            #            validate=lambda x: x != ""
        ),
        inquirer.Text(
            "tooltip",
            message="Tooltip for the new {input_type}",
            default="{placeholder}"
            #            validate=lambda x: x != ""
        ),
    ]

    set_output = [
        inquirer.List(
            "output_type",
            message="Set output type",
            choices=["image", "text", "sound", "video"],
            default="image",
        ),
        inquirer.Text(
            "output_name",
            message="Output name for the {output_type}",
            default="{output_type}"
            #            validate=lambda x: x != ""
        ),
        inquirer.Text(
            "example_value",
            message="{output_type} Example Value",
            default="{output_type}"
            #            validate=lambda x: x != ""
        ),
    ]

    inputs = list()
    output = dict()

    if not task_exists(input_type, output_type, task_name):
        add_element = [
            inquirer.List(
                "element",
                message=f"Set a new element variables for the task {task_name}",
                choices=["input", "output", "done"],
            )
        ]
        added_element = dict()
        added_element["element"] = None
        while added_element["element"] != "done":
            added_element = inquirer.prompt(add_element, theme=GreenPassion())
            if added_element["element"] == "input":
                inputs.append(inquirer.prompt(set_input, theme=GreenPassion()))
            elif added_element["element"] == "output":
                output = inquirer.prompt(set_output, theme=GreenPassion())
            else:
                create_task_routeur(input_type, output_type, task_name, inputs, output)
                print("done defining environment")

    else:
        print(f"Task {task_name} already exists")

    return input_type, output_type, task_name, inputs, output


def scaffold_model(input_type, output_type, task_name, inputs, output):
    set_model_name = [
        inquirer.Text(
            "model_name",
            message="Set model name",
            default="model_name_without_no_space_dash_only",
        )
    ]

    model_name = inquirer.prompt(set_model_name, theme=GreenPassion())["model_name"]

    if not model_exists(input_type, output_type, task_name, model_name):
        model_file = create_model(
            input_type, output_type, task_name, model_name, inputs, output
        )
    else:
        print(f"Model {model_name} already exists")
    return model_file


if __name__ == "__main__":

    input_type, output_type, task_name, inputs, output = scaffold_task()
    model_file = scaffold_model(input_type, output_type, task_name, inputs, output)

    print(f"you can now edit {model_file}")
