import importlib
import json
import logging
import os
import pkgutil

from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.security.oauth2 import (OAuth2, OAuthFlowsModel,
                                     get_authorization_scheme_param)
from fastapi_utils.timing import add_timing_middleware, record_timing
from icecream import ic
from prometheus_fastapi_instrumentator import Instrumentator, metrics
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse

import apis
import os
from fastapi.responses import ORJSONResponse

from pattern.text.en import singularize

config_file = os.getenv('API_CONFIG_FILE', 'config.json')


if os.path.isfile(config_file):
    with open("config.json", "r") as f:
        config = json.load(f)

try:
    logging.basicConfig(level=logging.INFO, format=config["logs"]["log_format"])
except:
    logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)



app = FastAPI(default_response_class=ORJSONResponse)

if config["prometheus"]["active"]:
    instrumentator = Instrumentator(
        should_group_status_codes=config["prometheus"]["instrumentator"][
            "should_group_status_codes"
        ],
        should_ignore_untemplated=config["prometheus"]["instrumentator"][
            "should_ignore_untemplated"
        ],
        should_group_untemplated=config["prometheus"]["instrumentator"][
            "should_group_untemplated"
        ],
        should_respect_env_var=config["prometheus"]["instrumentator"][
            "should_respect_env_var"
        ],
        env_var_name=config["prometheus"]["instrumentator"]["env_var_name"],
        excluded_handlers=config["prometheus"]["instrumentator"]["excluded_handlers"],
        should_round_latency_decimals=config["prometheus"]["instrumentator"][
            "should_round_latency_decimals"
        ],
        round_latency_decimals=config["prometheus"]["instrumentator"][
            "round_latency_decimals"
        ],
        should_instrument_requests_inprogress=config["prometheus"]["instrumentator"][
            "should_instrument_requests_inprogress"
        ],
        inprogress_name=config["prometheus"]["instrumentator"]["inprogress_name"],
        inprogress_labels=config["prometheus"]["instrumentator"]["inprogress_labels"],
    )


if config["logs"]["timing_activated"]:
    add_timing_middleware(app, record=logger.info, prefix="app")


app.add_middleware(
    CORSMiddleware,
    allow_origins=config["CORS"]["allow_origins"],
    allow_credentials=config["CORS"]["allow_credentials"],
    allow_methods=config["CORS"]["allow_methods"],
    allow_headers=config["CORS"]["allow_headers"],
)


def import_submodules(package, recursive=True):
    global active_tasks

    if isinstance(package, str):
        current_package = package.split(".")
        package = importlib.import_module(package)

    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + "." + name
        this_module = importlib.import_module(full_name)
        module_short_name = full_name.replace("apis", "")[1:]

        if "router" in dir(this_module):
            module_input, module_output, module_task = module_short_name.split(".")
            module_task = singularize(module_task).upper()
            active_task_list = list(
                map(
                    lambda each: singularize(each).upper(),
                    config["active_tasks"][module_input][module_output],
                )
            )

            if "None".upper() not in active_task_list and (
                "*" in config["active_tasks"][module_input][module_output]
                or module_task in active_task_list
            ):

                module_prefix = full_name.replace(".", "/").replace("apis", "")
                ic(f"Loading module: {full_name}")
                app.include_router(this_module.router, prefix=module_prefix)

        if recursive and is_pkg:
            ic(module_short_name)
            module_split = module_short_name.split(".")

            if len(module_split) == 1:
                import_submodules(full_name)
            elif (
                len(module_split) == 2
                and "None".upper
                not in map(
                    lambda each: each.upper(),
                    config["active_tasks"][module_split[0]][module_split[1]],
                )
                or len(config["active_tasks"][module_split[0]][module_split[1]]) == 0
            ):
                ic(f"importing {full_name}")
                import_submodules(full_name)
            elif len(module_split) == 3 and (
                module_split[2].rstrip("s")
                in map(
                    lambda each: each.rstrip("s"),
                    config["active_tasks"][module_split[0]][module_split[1]],
                )
                or "*" in config["active_tasks"][module_split[0]][module_split[1]]
            ):
                ic(f"importing {full_name}")
                import_submodules(full_name)
            elif len(module_split) == 4:
                ic(f"importing {full_name}")
                import_submodules(full_name)
            else:
                ic(f"skipping {module_short_name}")


import_submodules(apis)
