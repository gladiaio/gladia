import os
import yaml
import subprocess

from gladia_api_utils import get_activated_task_path


def create_custom_env(env_name: str, path_to_env_file: str) -> None:
    custom_env = yaml.safe_load(open(path_to_env_file, "r"))

    try:
        # TODO: adding a python version should be optional
        subprocess.run(f"micromamba create -n {env_name} -c conda-forge python={custom_env['python']}".split(" "), check=True)

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't create env {env_name}: {error}")

    try:
        subprocess.run(f"micromamba run -n {env_name} pip install {' '.join(custom_env['packages'])}".split(" "), check=True)

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't install dependencies for env {env_name}: {error}")


def main():
    paths = get_activated_task_path(
        path_to_config_file="../config.json",
        path_to_apis="../apis"
    )


    for task in paths:
        models = list(filter(lambda dir : os.path.split(dir)[-1][0] not in ['_', '.'], os.listdir(task)))

        for model in models:
            if "env.yaml" not in os.listdir(os.path.join(task, model)):
                continue

            create_custom_env(
                env_name=f"{os.path.split(task)[-1]}-{model}",
                path_to_env_file=os.path.join(task, model, 'env.yaml')
            )


if __name__ == "__main__":
    main()
