from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter


input = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to blur face from",
        "placeholder": "Image to blur face from",
        "tooltip": "Image to blur face from",
    }
]

output = {
        "name": "blured_image",
        "type": "image",
        "example": "image"
    }

router = APIRouter()

TaskRouter(router=router, input=input, output=output, default_model="v1")
