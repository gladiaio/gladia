from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "http://files.gladia.io/test/test.png",
        "placeholder": "Image to uncolorize",
        "tooltip": "Insert the image to uncolorize",
    }
]

output = {"name": "uncolorized_image", "type": "image", "example": "uncolorized_image"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="v1")
