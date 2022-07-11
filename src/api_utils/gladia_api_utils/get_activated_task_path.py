import json
import os


def list_tasks_for_modalities(
    root_path: str, input_modaliy: str, output_modaliy: str
) -> str:
    """List every tasks (activated or not) for a certain input/output modality pair

    Args:
        root_path (str): path to the apis' root folder
        input_modaliy (str): modality of the model input
        output_modaliy (str): modality of the model output

    Returns:
        str: path to the tasks founded for the input/output modality pair
    """

    tasks = os.listdir(os.path.join(root_path, input_modaliy, output_modaliy))

    paths = [
        os.path.join(root_path, input_modaliy, output_modaliy, task) for task in tasks
    ]

    paths = list(
        filter(
            lambda dir: os.path.split(dir)[-1][0] not in ["_", "."]
            and os.path.isdir(dir),
            paths,
        )
    )

    return paths


def get_activated_task_path(path_to_config_file: str, path_to_apis: str) -> str:
    """Return the path to each task folder that is activated in the config.json file

    Args:
        path_to_config_file (str): path to the config.json file
        path_to_apis (str): path to the apis' root folder

    Returns:
        str: a list of path to each activated task
    """

    config = json.load(open(path_to_config_file))

    tasks = set()
    for input_modaliy in config["active_tasks"].keys():
        for output_modaliy in config["active_tasks"][input_modaliy].keys():
            active_tasks = config["active_tasks"][input_modaliy][output_modaliy]

            if "NONE" in active_tasks:
                continue

            if "*" in active_tasks:
                paths = list_tasks_for_modalities(
                    path_to_apis, input_modaliy, output_modaliy
                )
            else:
                paths = [
                    os.path.join(path_to_apis, input_modaliy, output_modaliy, task)
                    for task in active_tasks
                ]

            tasks = tasks.union(set(paths))

    return tasks
