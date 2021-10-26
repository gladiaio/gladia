from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

input = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to restore",
        "placeholder": "Image to restore",
        "tooltip": "Insert the image to restore",
    },
]

output = {
        "name": "enhanced_image",
        "type": "image",
        "example": "enhanced_image"
    }

router = APIRouter()

TaskRouter(router=router, input=input, output=output, default_model="esrgan")
