import os
import yaml
import tempfile
import subprocess

from tqdm import tqdm
from typing import Tuple, List
from gladia_api_utils import get_activated_task_path


def retrieve_package_from_env_file(env_file: dict) -> Tuple[List[str], List[str]]:
    packages_to_install_from_pip = []
    packages_to_install_from_channel = []

    for idx, package in enumerate(env_file["dependencies"]):
        if type(package) == dict and "pip" in package.keys():
            for pip_package in package["pip"]:
                packages_to_install_from_pip.append(pip_package)
        else:
            packages_to_install_from_channel.append(package)

    return packages_to_install_from_pip, packages_to_install_from_channel


def create_temp_env_file(
    env_name: str,
    packages_to_install_from_channel: List[str],
    packages_to_install_from_pip: List[str]
) -> str:

    tmp = tempfile.NamedTemporaryFile(delete=False)

    content = """
name: """ + env_name + """

dependencies:""" + ''.join([f"\n  - {package}" for package in packages_to_install_from_channel])+ """
  - pip:""" + ''.join([f"\n    - {package}" for package in packages_to_install_from_pip])

    with open(tmp.name, "w") as f:
        f.write(content)

    tmp.close()

    return tmp


def create_custom_env(env_name: str, path_to_env_file: str) -> None:
    print(f"Creating env : {env_name}")

    custom_env = yaml.safe_load(open(path_to_env_file, "r"))

    packages_to_install_from_pip, packages_to_install_from_channel = retrieve_package_from_env_file(custom_env)

    if "inherit" not in custom_env.keys():
        custom_env["inherit"] = []

    for env_to_inherit in custom_env["inherit"]:

        path_to_env_to_inherit_from = os.path.join(
            os.path.split(os.path.abspath(__file__))[0],
            "envs",
            env_to_inherit.split("-")[0],
            '-'.join(env_to_inherit.split("-")[1:]) + ".yaml"
        )

        env_file = yaml.safe_load(open(path_to_env_to_inherit_from, "r"))
        pip_packages, channel_packages = retrieve_package_from_env_file(env_file)

        packages_to_install_from_pip += pip_packages
        packages_to_install_from_channel += channel_packages

    temporary_file = create_temp_env_file(
        env_name,
        packages_to_install_from_channel,
        packages_to_install_from_pip
    )

    os.link(temporary_file.name, temporary_file.name + ".yaml")

    try:
        subprocess.run(f"micromamba create -f {temporary_file.name  + '.yaml'} -y".split(" "), check=True)

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't create env {env_name}: {error}")

    finally:
        os.remove(temporary_file.name)
        os.remove(temporary_file.name + ".yaml")


def main():
    paths = get_activated_task_path(
        path_to_config_file="../config.json",
        path_to_apis="../apis"
    )

    for task in tqdm(paths):

        if os.path.exists(os.path.join(task, "env.yaml")):
            create_custom_env(
                env_name=os.path.split(task)[1],
                path_to_env_file=os.path.join(task, "env.yaml")
            )

        models = list(filter(lambda dir : os.path.split(dir)[-1][0] not in ['_', '.'], os.listdir(task)))

        for model in models:
            if not os.path.exists(os.path.join(task, model, "env.yaml")):
                continue

            create_custom_env(
                env_name=f"{os.path.split(task)[-1]}-{model}", # FIXME: il y a aura un conflit entre le nom du dossier qui est au pluriel et le nom de la route qui est au singulier
                path_to_env_file=os.path.join(task, model, 'env.yaml')
            )


if __name__ == "__main__":
    main()
