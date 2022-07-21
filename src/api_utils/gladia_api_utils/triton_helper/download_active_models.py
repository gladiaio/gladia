import os
import shutil
import json
import subprocess

from time import time


def __filter_directories(directories: [str]) -> [str]:
    """
    Remove hidden directories from `directories`

    :param directories: directories to remove hidden dir from
    """

    return list(filter(lambda dir_name: not dir_name[0] in ["_", "."], directories))


def __get_every_models_path_for_given_task(
    root_path: str, input_modality: str, output_modality: str, task: str
) -> [str]:
    """Return a list of path leading to each model for a certain task

    Args:
        root_path (str): path to the root of apis
        input_modality (str): modality of the input of `task
        output_modality (str): modality of the output of `task`
        task (str): task to get the models from

    Returns:
        [str]: list of path leading to each model for a certain task
    """

    models_path = []

    directories = os.listdir(
        os.path.join(root_path, input_modality, output_modality, task)
    )
    directories = __filter_directories(directories)
    directories = [
        directory
        for directory in directories
        if os.path.isdir(
            os.path.join(root_path, input_modality, output_modality, task, directory)
        )
    ]

    for directory in directories:
        models_path.append(
            os.path.join(
                root_path, input_modality, output_modality, task, directory, ".git_path"
            )
        )

    return models_path


def __get_active_models_path_for_modality(
    root_path: str, input_modality: str, output_modality: str, actives: [str]
) -> [str]:
    """Return path to each activated model for a certain modality

    Args:
        root_path (str): path to the root of apis
        input_modality (str): modality of the input
        output_modality (str): modality of the output
        actives (str]): list listing each activated task

    Returns:
        [str]: path to each activated model across every tasks that is activated
    """

    if "NONE" in actives:
        return []

    if "*" in actives:
        actives = __filter_directories(
            os.listdir(os.path.join(root_path, input_modality, output_modality))
        )
        actives = [
            active
            for active in actives
            if os.path.isdir(
                os.path.join(root_path, input_modality, output_modality, active)
            )
        ]
    else:
        actives = [activity + "s" for activity in actives]

    models_path = []
    for task in actives:
        models_path = models_path + __get_every_models_path_for_given_task(
            root_path, input_modality, output_modality, task
        )

    return models_path


def __get_active_models_path(rooth_path: str, active_tasks: [str]) -> [str]:
    """Return a list of path to each model that is activated

    Args:
        rooth_path (str): path to the root of apis
        active_tasks (str]): path to the root of apis

    Returns:
        [str]: list of path to each model that is activated
    """

    models_path = []

    for input_modality in active_tasks.keys():
        for output_modality in active_tasks[input_modality].keys():
            models_path = models_path + __get_active_models_path_for_modality(
                rooth_path,
                input_modality,
                output_modality,
                active_tasks[input_modality][output_modality],
            )

    return models_path


def download_triton_model(triton_models_dir: str, git_path: str) -> None:
    """Download a model stored on git (with lfs) and extract it to `triton_models_dir`

    Args:
        triton_models_dir (str): Where to download and extract the model to
        git_path (str): file containing the http/ssh route of the git containing the model to download
    """

    if not os.path.exists(git_path):
        return

    git_url = open(git_path).read()

    clone_to_path = os.path.join("/tmp/", str(time()))

    subprocess.run(f"git clone {git_url} {clone_to_path}", shell=True, check=True)

    subprocess.run(
        f"cd {clone_to_path} && git lfs fetch && git lfs pull", shell=True, check=True
    )

    already_downloaded_models = os.listdir(triton_models_dir)

    for filename in os.listdir(clone_to_path):
        if filename[0] == "." or filename in already_downloaded_models:
            continue

        shutil.move(os.path.join(clone_to_path, filename), triton_models_dir)

    shutil.rmtree(clone_to_path)


def download_active_triton_models(
    triton_models_dir: str, config_file_path: str
) -> None:
    """Download every models stored in git (with lfs) by reading each `.git_path` files

    Args:
        triton_models_dir (str): Where to download and extract the models
        config_file_path (str): Config file describing wich task is activated
    """

    config_file = json.load(open(config_file_path))

    for model_path in __get_active_models_path("./apis", config_file["active_tasks"]):
        download_triton_model(triton_models_dir, model_path)
