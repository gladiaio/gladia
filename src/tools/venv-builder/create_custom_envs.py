import os
import re
import yaml
import logging
import argparse
import tempfile
import subprocess

from tqdm import tqdm
from typing import List, Tuple
from gladia_api_utils import get_activated_task_path


logger = logging.getLogger(__name__)


def retrieve_package_from_env_file(env_file: dict) -> Tuple[List[str], List[str]]:
    packages_to_install_from_pip = []
    packages_to_install_from_channel = []

    if env_file is None or "dependencies" not in env_file.keys():
        return packages_to_install_from_pip, packages_to_install_from_channel

    for package in env_file["dependencies"]:
        if type(package) == dict and "pip" in package.keys():
            for pip_package in package["pip"]:
                packages_to_install_from_pip.append(pip_package)
        else:
            packages_to_install_from_channel.append(package)

    return packages_to_install_from_pip, packages_to_install_from_channel


def create_temp_env_file(
    env_name: str,
    packages_to_install_from_channel: List[str],
    packages_to_install_from_pip: List[str],
) -> str:

    tmp = tempfile.NamedTemporaryFile(delete=False)

    content = (
        """
name: """
        + env_name
        + """

dependencies:"""
        + "".join([f"\n  - {package}" for package in packages_to_install_from_channel])
    )

    if (
        packages_to_install_from_pip is not None
        and len(packages_to_install_from_pip) > 0
    ):
        content += """
  - pip:""" + "".join(
            [f"\n    - {package}" for package in packages_to_install_from_pip]
        )

    with open(tmp.name, "w") as f:
        f.write(content)

    tmp.close()

    return tmp


def create_custom_env(env_name: str, path_to_env_file: str) -> None:
    logger.debug(f"Creating env : {env_name}")

    custom_env = yaml.safe_load(open(path_to_env_file, "r"))

    if custom_env is None:
        error_message = "Provided config env is empty, you must either specify `inherit` or `dependencies`."

        logger.error(error_message)

        raise RuntimeError(error_message)

    (
        packages_to_install_from_pip,
        packages_to_install_from_channel,
    ) = retrieve_package_from_env_file(custom_env)

    if "inherit" not in custom_env.keys():
        custom_env["inherit"] = []

    for env_to_inherit in custom_env["inherit"]:

        path_to_env_to_inherit_from = os.path.join(
            os.path.split(os.path.abspath(__file__))[0],
            "envs",
            env_to_inherit.split("-")[0],
            "-".join(env_to_inherit.split("-")[1:]) + ".yaml",
        )

        env_file = yaml.safe_load(open(path_to_env_to_inherit_from, "r"))
        pip_packages, channel_packages = retrieve_package_from_env_file(env_file)

        packages_to_install_from_pip += pip_packages
        packages_to_install_from_channel += channel_packages

    temporary_file = create_temp_env_file(
        env_name, packages_to_install_from_channel, packages_to_install_from_pip
    )

    os.link(temporary_file.name, temporary_file.name + ".yaml")

    try:
        subprocess.run(
            f"micromamba create -f {temporary_file.name  + '.yaml'} -y".split(" "),
            check=True,
        )
        subprocess.run(
            f"micromamba clean --all --yes".split(" "),
            check=True,
        )

    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"Couldn't create env {env_name}: {error}")

    finally:
        os.remove(temporary_file.name)
        os.remove(temporary_file.name + ".yaml")

        logger.info("Env {env_name} has been successfully created")


def build_specific_envs(paths: List[str]) -> None:
    """Build mamba envs using the provided {paths}

    Arguments:
        paths {List[str]} -- List of path to either a model folder or a model's env file (env.yaml)

    Raises:
        FileNotFoundError: The profided model folder or env file couldn't be founded
    """

    paths = set(paths)

    for path in paths:

        if not os.path.exists(path):
            raise FileNotFoundError(
                f"custom env {path} not found, please specify a correct path either leading to a model or model's env file."
            )

        if "env.yaml" in path:
            path = os.path.split(path)[0]

        task_path, model = os.path.split(path)
        task = os.path.split(task_path)[1]
        
        logger.debug("building", f"{task}-{model}")

        create_custom_env(
            env_name=f"{task}-{model}", path_to_env_file=os.path.join(path, "env.yaml")
        )


def build_env_for_activated_tasks(
    path_to_config_file: str, path_to_apis: str, modality=".*"
) -> None:
    """Build the mamba env for every activated tasks

    Arguments:
        path_to_config_file {str} -- Path to the general config file describing which tasks is activated
        path_to_apis {str} -- Path to the Gladia's tasks
        modality {str} -- modality name pattern filter
    """

    paths = get_activated_task_path(
        path_to_config_file=path_to_config_file, path_to_apis=path_to_apis
    )

    for task in tqdm(paths):

        if not bool(re.search(modality[0], task)):
            logger.debug(f"Skipping task {task}")

            continue

        if os.path.exists(os.path.join(task, "env.yaml")):
            create_custom_env(
                env_name=os.path.split(task)[1],
                path_to_env_file=os.path.join(task, "env.yaml"),
            )

        models = list(
            filter(
                lambda dir: os.path.split(dir)[-1][0] not in ["_", "."],
                os.listdir(task),
            )
        )

        for model in models:
            if not os.path.exists(os.path.join(task, model, "env.yaml")):
                continue

            create_custom_env(
                env_name=f"{os.path.split(task)[-1]}-{model}",  # FIXME: il y a aura un conflit entre le nom du dossier qui est au pluriel et le nom de la route qui est au singulier
                path_to_env_file=os.path.join(task, model, "env.yaml"),
            )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--name",
        action="append",
        type=str,
        help="Specify the name of a specific env to build. You can define this arg multiple time to build multiple specific envs.",
    )
    parser.add_argument(
        "--modality",
        action="append",
        type=str,
        help="Specify a RegExp to filter input nd output modalities to process. default .*",
    )
    parser.add_argument(
        "--path_to_apis",
        action="append",
        type=str,
        help="Specify a path to the api app .*",
    )
    args = parser.parse_args()

    if args.name:
        return build_specific_envs(args.name)

    if args.path_to_apis:
        path_to_apis = args.path_to_apis
    else:
        path_to_apis = "/app/apis"

    return build_env_for_activated_tasks(
        path_to_config_file=f"{path_to_apis}/../config.json",
        path_to_apis=path_to_apis,
        modality=args.modality,
    )


if __name__ == "__main__":
    main()
