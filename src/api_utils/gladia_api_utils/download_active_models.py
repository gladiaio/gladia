import os
import json


def __filter_directories(directories: [str]) -> [str]:
    return list(filter(lambda dir_name: not dir_name[0] in ["_", "."], directories))


def __get_every_models_path_for_given_task(root_path, input_modality, output_modality, task) -> [str]:
    models_path = []

    directories = os.listdir(os.path.join(root_path, input_modality, output_modality, task))
    directories = __filter_directories(directories)
    directories = [directory for directory in directories if os.path.isdir(os.path.join(root_path, input_modality, output_modality, task, directory))]

    for directory in directories:
        models_path.append(os.path.join(root_path, input_modality, output_modality, task, directory, ".git_path"))

    return models_path


def __get_active_models_path_for_task(root_path, input_modality, output_modality, actives) -> [str]:
    if "NONE" in actives:
        return []

    if "*" in actives:
        actives = __filter_directories(os.listdir(os.path.join(root_path, input_modality, output_modality)))
        actives = [active for active in actives if os.path.isdir(os.path.join(root_path, input_modality, output_modality, active))]

    models_path = []
    for task in actives:
        models_path = models_path + __get_every_models_path_for_given_task(root_path, input_modality, output_modality, task)

    return models_path


def __get_active_models_path(rooth_path, active_tasks) -> [str]:
    models_path = []

    for input_modality in active_tasks.keys():
        for output_modality in active_tasks[input_modality].keys():
            models_path = models_path + __get_active_models_path_for_task(rooth_path, input_modality, output_modality, active_tasks[input_modality][output_modality])

    return models_path
            

def download_triton_model(triton_models_dir, git_path: str) -> None:
    if not os.path.exists(git_path):
        return

    git_url = open(git_path).read()
    model_name = git_url.split("/")[-1]

    clone_to_path = os.path.join(triton_models_dir, model_name)

    if os.path.exists(clone_to_path):
        return
    
    os.system(f"git clone {git_url} {clone_to_path}")


def download_active_triton_models(triton_models_dir, config_file_path: str) -> None:
    config_file = json.load(open(config_file_path))

    for model_path in __get_active_models_path("./apis", config_file["active_tasks"]):
        download_triton_model(triton_models_dir, model_path)
