import os
import yaml
import subprocess

from gladia_api_utils import get_activated_task_path


def create_custom_env(env_name: str, path_to_env_file: str) -> None:
    try:
        subprocess.run(f"micromamba create -n {env_name}".split(" "), check=True)

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't create env {env_name}: {error}")

    custom_env = yaml.safe_load(open(path_to_env_file, "r"))

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


def exec_in_custom_env(path_to_env_file: str, cmd: str):
    path = path_to_env_file.split("/")

    task = path[-3]
    model = path[-2]

    env_name = f"{task}-{model}"

    env_cfg = yaml.safe_load(open(path_to_env_file))

    env_to_inherite_from = ''
    if "inheritance" in env_cfg.keys() and len(env_cfg['inheritance']) > 0:
        env_to_inherite_from = "micromamba activate " + "&& micromamba activate --stack ".join(env_cfg["inheritance"])

        cmd = f"{env_to_inherite_from} && micromamba activate --stack {env_name} && {cmd}"

    else:
        cmd = f"micromamba activate {env_name} && {cmd}"

    try:
        os.system("""eval "$(micromamba shell hook --shell=bash)" && """ + cmd)

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't activate custom env {env_name}: {error}")


if __name__ == "__main__":
    main()
