import os
import json
import subprocess


def create_env_from_yaml(path_to_yaml: str) -> None:
    command = "micromamba create -f".split(" ")

    try:
        subprocess.run([*command, path_to_yaml])

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't install env using micromamba: {error}")

def create_env_for_modality(path_to_modality_env_folder: str) -> None:
    files = os.listdir(path_to_modality_env_folder)

    yaml_files = list(filter(
        lambda filename: filename[0] not in ['.', '_'] and len(filename) > 5 and filename[-5:] == ".yaml",
        files
    ))

    for path_to_yaml in yaml_files:
        create_env_from_yaml(os.path.join(path_to_modality_env_folder, path_to_yaml))


def get_activated_modalities() -> (str):
    config = json.load(open("../config.json", "r"))

    modalities = set()
    for input_modaliy in config["active_tasks"].keys():
        for output_modaliy in config["active_tasks"][input_modaliy].keys():
            tasks = config["active_tasks"][input_modaliy][output_modaliy]
    
            if len(tasks) > 0 and "NONE" not in tasks:
                modalities.add(input_modaliy)
                modalities.add(output_modaliy)

                break

    return modalities


def main():
    modalities = get_activated_modalities()

    for path in (os.path.join(os.getcwd(), "envs", modality) for modality in modalities):
        create_env_for_modality(path)


if __name__ == "__main__":
    main()
