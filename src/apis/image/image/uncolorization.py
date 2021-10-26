from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

input = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to uncolorize",
        "placeholder": "Image to uncolorize",
        "tooltip": "Insert the image to uncolorize",
    },
]

output = {
        "name": "uncolorized_image",
        "type": "image",
        "example": "uncolorized_image"
    }

router = APIRouter()

TaskRouter(router=router, input=input, output=output, default_model="v1")
