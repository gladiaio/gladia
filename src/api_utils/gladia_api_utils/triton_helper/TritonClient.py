import os
import requests
import tritonclient.http as tritonclient

from time import sleep
from typing import Any
from warnings import warn
from .download_active_models import download_triton_model


class TritonClient():
    """Wrapper suggaring triton'client usage
    """

    def __init__(self, model_name: str, current_path: str = "") -> None:
        """TritonClient's initializer

        Args:
            model_name (str): name of the model to communicate with
            current_path (str, optional): current path (allows to download model if needed). Defaults to "".
        """

        self.__model_name = model_name
        self.__triton_server_url = os.getenv("TRITON_SERVER_URL")

        if not self.__triton_server_url:
            raise RuntimeError("URL of the triton server not specified")

        self.__client = tritonclient.InferenceServerClient(url=self.__triton_server_url, verbose=False)

        self.__registered_inputs = []

        self.__registered_outputs = [
            tritonclient.InferRequestedOutput(
               name=f'output__0',
            ),
        ]


        if os.getenv('TRITON_MODELS_PATH') == "":
            warn("[DEBUG] TRITON_MODELS_PATH is not set, please specify it in order to be able to download models.")

        self.__download_model(os.path.join(current_path, ".git_path"))

    @property
    def client(self):
        return self.__client

    def register_new_input(self, shape, datatype: str) -> None:
        """Add a new input to the triton inferer. Each input has to be registered before usage.

        Args:
            shape (int, ...): shape of the input to register
            datatype (str): datatype of the input to register
        """

        self.__registered_inputs.append(tritonclient.InferInput(
            name=f'input__{len(self.__registered_inputs)}',
            shape=shape,
            datatype=datatype
        ))

    def register_new_output(self) -> None:
        """Add a new output to the triton inferer. Each ouput has to be registered before usage.\n
        By default one ouput named `output__0` is already registered.
        """

        self.__registered_outputs.append(tritonclient.InferRequestedOutput(
            name=f'ouput__{len(self.__registered_outputs)}',
        ))

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
            if model['name'] == self.__model_name:
                return
        
        warn('Downloading model from hugging-face, to prevent lazy downloading please specify TRITON_LAZY_DOWNLOAD=False')

        download_triton_model(
            triton_models_dir=os.getenv('TRITON_MODELS_PATH'),
            git_path=path_to_git_path_file
        )

        sleep(sleep_time)

    def __call__(self, *args, **kwds) -> [Any]:
        """Call the triton inferer with the inputs in `args`.

        Returns:
            [Any]: List of outputs from the model
        """
        del kwds

        for arg, registered_input in zip(args, self.__registered_inputs):
            registered_input.set_data_from_numpy(arg)

        requests.post(url=f"http://{self.__triton_server_url}/v2/repository/models/{self.__model_name}/load")

        model_response = self.client.infer(
            self.__model_name,
            model_version='1',
            inputs=self.__registered_inputs,
            outputs=self.__registered_outputs
        )

        response = requests.post(
            url=f"http://{self.__triton_server_url}/v2/repository/models/{self.__model_name}/unload",
            data={
                "unload_dependents": True,
            }
        )

        if response.status_code != 200:
            warn(f"{self.__model_name} has not been properly unloaded.")

        return [model_response.as_numpy(output.name())[0] for output in self.__registered_outputs]
