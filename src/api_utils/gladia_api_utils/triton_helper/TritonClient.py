import os
import pathlib
import sys
from time import sleep
from typing import Any
from warnings import warn

import requests
import tritonclient.http as tritonclient

from .download_active_models import download_triton_model


class TritonClient:
    """Wrapper suggaring triton'client usage"""

    def __init__(
        self,
        model_name: str,
        **kwargs,
    ) -> None:
        """TritonClient's initializer

        Args:
            triton_server_url (str): URL to the triton server
            model_name (str): name of the model to communicate with
            current_path (str, optional): current path (allows to download model if needed). Defaults to "".
        """

        self.__triton_server_url = kwargs.get(
            "triton_server_url",
            os.getenv("TRITON_SERVER_URL", default="localhost:8000"),
        )

        self.__current_path = kwargs.get(
            "current_path",
            str(
                pathlib.Path(sys._getframe(1).f_globals["__file__"])
                .parents[0]
                .absolute()
            ),
        )

        self.__model_name = model_name
        self.__model_sub_parts = kwargs.get("sub_parts", [])

        self.__preload_model: bool = kwargs.get("preload_model", False)

        if self.__preload_model and not self.load_model():
            warn(
                f"{self.__model_name} has not been properly loaded. Setting back lazy load to True"
            )

            self.__preload_model = False

        self.__client = tritonclient.InferenceServerClient(
            url=self.__triton_server_url, verbose=False
        )

        self.__registered_inputs = {}

        self.__registered_outputs = [
            tritonclient.InferRequestedOutput(
                name=kwargs.get("output_name", "output__0")
            )
        ]

        if os.getenv("TRITON_MODELS_PATH") == "":
            warn(
                "[DEBUG] TRITON_MODELS_PATH is not set, please specify it in order to be able to download models."
            )

        self.__download_model(os.path.join(self.__current_path, ".git_path"))

    @property
    def client(self):
        return self.__client

    def load_model(self) -> bool:
        """Requests triton to load the model

        Returns:
            bool: whether the model has been successfully loaded or not
        """

        for model_sub_part in self.__model_sub_parts:
            response = requests.post(
                url=f"http://{self.__triton_server_url}/v2/repository/models/{model_sub_part}/load",
            )

            if response.status_code != 200:
                return False

        response = requests.post(
            url=f"http://{self.__triton_server_url}/v2/repository/models/{self.__model_name}/load"
        )

        return response.status_code == 200

    def unload_model(self) -> bool:
        """Requests triton to unload the model

        Returns:
            bool: whether the model has been successfully unloaded or not
        """

        successfully_unload_model: bool = True

        response = requests.post(
            url=f"http://{self.__triton_server_url}/v2/repository/models/{self.__model_name}/unload",
            data={"unload_dependents": False},
        )

        if response.status_code != 200:
            successfully_unload_model = False

        for model_sub_part in self.__model_sub_parts:
            response = requests.post(
                url=f"http://{self.__triton_server_url}/v2/repository/models/{model_sub_part}/unload",
            )

            if response.status_code != 200:
                successfully_unload_model = False

        return successfully_unload_model

    def set_input(self, shape, datatype: str, **kwargs) -> None:
        """Add a new input to the triton inferer. Each input has to be registered before usage.

        Args:
            shape (int, ...): shape of the input to register
            datatype (str): datatype of the input to register
        """

        input_name = kwargs.get("name", f"input__{len(self.__registered_inputs)}")
        self.__registered_inputs[input_name] = tritonclient.InferInput(
            name=input_name, shape=shape, datatype=datatype
        )

    def unset_input(self, input_name: str):
        del self.__registered_inputs[input_name]

    def register_new_output(self, **kwargs) -> None:
        """Add a new output to the triton inferer. Each ouput has to be registered before usage.\n
        By default one ouput named `output__0` is already registered.
        """

        self.__registered_outputs.append(
            tritonclient.InferRequestedOutput(
                name=kwargs.get("name", f"ouput__{len(self.__registered_outputs)}")
            )
        )

    def __download_model(self, path_to_git_path_file: str, sleep_time: int = 0) -> None:
        """Check if the model need to be downloaded, if so download and extract it.

        Args:
            path_to_git_path_file (str): path to the `.git_path` file
            sleep_time (int, optional): sleep time after extracting the model. Defaults to 0.
        """

        response = requests.post(
            url=f"http://{self.__triton_server_url}/v2/repository/index"
        )

        for model in response.json():
            if model["name"] == self.__model_name:
                return

        warn(
            "Downloading model from hugging-face, to prevent lazy downloading please specify TRITON_LAZY_DOWNLOAD=False"
        )

        download_triton_model(
            triton_models_dir=os.getenv("TRITON_MODELS_PATH"),
            git_path=path_to_git_path_file,
        )

        sleep(sleep_time)

    def __call__(self, *args, **kwds) -> [Any]:
        """Call the triton inferer with the inputs in `args`.

        Returns:
            [Any]: List of outputs from the model
        """

        del kwds

        for arg, registered_input in zip(args, self.__registered_inputs.values()):
            registered_input.set_data_from_numpy(arg)

        if not self.__preload_model and not self.load_model():
            warn(
                f"{self.__model_name} has not been properly loaded. Returning empty response"
            )

            return [[]]

        model_response = self.client.infer(
            self.__model_name,
            model_version="1",
            inputs=self.__registered_inputs.values(),
            outputs=self.__registered_outputs,
        )

        if not self.__preload_model and not self.unload_model():
            warn(f"{self.__model_name} has not been properly unloaded.")

        return [
            model_response.as_numpy(output.name()).tolist()
            for output in self.__registered_outputs
        ]
