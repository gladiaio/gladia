from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to convert to ascii",
        "placeholder": "Image to convert to ascii",
        "tooltip": "Insert the image to convert to ascii",
    }
]

output = {"name": "asciified_image", "type": "text", "example": "asciified_image"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="ramesh-aditya")
