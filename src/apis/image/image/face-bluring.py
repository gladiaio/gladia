from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "http://files.gladia.io/test/test.png",
        "placeholder": "Image to blur face from",
        "tooltip": "Image to blur face from",
    }
]

output = {"name": "blured_image", "type": "image", "example": "image"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="ageitgey")
