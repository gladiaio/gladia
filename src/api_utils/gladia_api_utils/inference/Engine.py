from enum import Enum
from .triton_helper import TritonClient


class Engine(Enum):
    TRITON = TritonClient
