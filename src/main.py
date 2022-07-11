import importlib
import json
import logging
import os
import pkgutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi_utils.timing import add_timing_middleware
from icecream import ic
from prometheus_fastapi_instrumentator import Instrumentator

import apis


def __init_config() -> dict:
    """
    Load config file and return it as a dict.

    Default path is `config.json`, use API_CONFIG_FILE varenv to change it.

    :return: config dict
    """

    config_file = os.getenv("API_CONFIG_FILE", "config.json")

    if os.path.isfile(config_file):
        with open("config.json", "r") as f:
            return json.load(f)


def __init_logging(api_config: dict) -> logging.Logger:
    """
    Create a logging.Logger with it format set to config["logs"]["log_format"] f exist, else default.

    :param api_config: api config dict
    :return: logger initialized
    """

    try:
        logging.basicConfig(level=logging.INFO, format=api_config["logs"]["log_format"])
    except KeyError:
        logging.basicConfig(level=logging.INFO)

    return logging.getLogger(__name__)


def __init_prometheus_instrumentator(instrumentator_config: dict) -> Instrumentator:
    """
    Initialize the prometheus_fastapi_instrumentator.Instrumentator using api config dict
    :param instrumentator_config: instrumentator config
    :return: Initialized Instrumentator
    """

    return Instrumentator(
        should_group_status_codes=instrumentator_config["should_group_status_codes"],
        should_ignore_untemplated=instrumentator_config["should_ignore_untemplated"],
        should_group_untemplated=instrumentator_config["should_group_untemplated"],
        should_respect_env_var=instrumentator_config["should_respect_env_var"],
        env_var_name=instrumentator_config["env_var_name"],
        excluded_handlers=instrumentator_config["excluded_handlers"],
        should_round_latency_decimals=instrumentator_config[
            "should_round_latency_decimals"
        ],
        round_latency_decimals=instrumentator_config["round_latency_decimals"],
        should_instrument_requests_inprogress=instrumentator_config[
            "should_instrument_requests_inprogress"
        ],
        inprogress_name=instrumentator_config["inprogress_name"],
        inprogress_labels=instrumentator_config["inprogress_labels"],
    )


def __set_app_middlewares(api_app: FastAPI, api_config: dict) -> None:
    """
    Set up the api middlewares

    :param api_app: FastAPI representing the API
    :param api_config: config telling which middlewares to use
    """

    if api_config["logs"]["timing_activated"]:
        add_timing_middleware(api_app, record=logger.info, prefix="app")

    api_app.add_middleware(
        CORSMiddleware,
        allow_origins=api_config["CORS"]["allow_origins"],
        allow_credentials=api_config["CORS"]["allow_credentials"],
        allow_methods=api_config["CORS"]["allow_methods"],
        allow_headers=api_config["CORS"]["allow_headers"],
    )


def singularize(string: str) -> str:
    if string[-1] == "s":
        return string[:-1]

    return string


def __add_router(module: "module", module_path: str) -> None:
    """
    Add the module router to the API app

    :param module: module to get the router from
    :param module_path: name of the module
    """

    module_input, module_output, module_task = module_path.replace("apis", "")[
        1:
    ].split(".")

    module_task = singularize(module_task).upper()
    module_config = config["active_tasks"][module_input][module_output]

    active_task_list = list(map(lambda each: singularize(each).upper(), module_config))

    if "NONE" not in active_task_list and (
        module_task in active_task_list or "*" in module_config
    ):
        module_prefix = module_path.replace(".", "/").replace("apis", "")
        app.include_router(module.router, prefix=module_prefix)


def __module_is_an_input_type(split_module_path):
    return len(split_module_path) == 1


def __module_is_a_modality(split_module_path, module_config):
    return (
        len(split_module_path) == 2
        and "None".upper not in map(lambda each: each.upper(), module_config)
        or len(module_config) == 0
    )


def __module_is_a_task(split_module_path, module_config):
    return len(split_module_path) == 3 and (
        split_module_path[2].rstrip("s")
        in map(lambda each: each.rstrip("s"), module_config)
        or "*" in module_config
    )


def __module_is_a_model(split_module_path: [str]):
    return len(split_module_path) == 4


def import_submodules(package: "module", recursive: bool = True) -> None:
    """
    Import every task presents in the API by loading each submodule (recursively by default)

    :param package: root package to import every submodule from
    :param recursive: will load recursively if set to True (by default)
    """

    if isinstance(package, str):
        package = importlib.import_module(package)

    for _, name, is_pkg in pkgutil.walk_packages(package.__path__):

        module_path = f"{package.__name__}.{name}"
        module = importlib.import_module(module_path)

        module_relative_path = module_path.replace("apis", "")[1:]

        if "router" in dir(module):
            __add_router(module, module_path)

        if not recursive or not is_pkg:
            continue

        module_split = module_relative_path.split(".")
        module_config = (
            config["active_tasks"][module_split[0]][module_split[1]]
            if len(module_split) > 1
            else []
        )

        if (
            __module_is_an_input_type
            or __module_is_a_modality(module_split, module_config)
            or __module_is_a_task(module_split, module_config)
            or __module_is_a_model(module_split)
        ):
            import_submodules(module_path)
        else:
            ic(f"skipping {module_relative_path}")


os.environ["TRITON_MODELS_PATH"] = os.getenv(
    "TRITON_MODELS_PATH", default="/tmp/gladia/triton"
)

config = __init_config()
logger = __init_logging(config)

app = FastAPI(default_response_class=ORJSONResponse)

__set_app_middlewares(app, config)

if config["prometheus"]["active"]:
    instrumentator = __init_prometheus_instrumentator(
        config["prometheus"]["instrumentator"]
    )

import_submodules(apis)
