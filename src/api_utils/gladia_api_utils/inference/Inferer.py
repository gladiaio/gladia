import os

from typing import Any
from inspect import stack
from .Engine import Engine


class Inferer:
    """Generic inferer class that instantiate the client to the target engine
    """

    def __init__(self, engine: Engine, model_name: str) -> None:
        """Instantiate te Inferer class to communicate with the target `engine`.

        Args:
            engine (Engine): engine to use
            model_name (str): name of the model to communicate with
        """

        self.__engine = engine.value(
            model_name=model_name,
            model_path = os.path.split(stack()[1].filename)[0]
        )
    
    def __call__(self, *args: Any, **_: Any) -> Any:
        return self.__engine(*args)

    @property
    def engine(self):
        return self.__engine
