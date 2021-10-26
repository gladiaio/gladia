from fastapi import APIRouter

from unifai_api_utils.submodules import TaskRouter


input = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to background removal",
        "placeholder": "Image to background removal",
        "tooltip": "Image to background removal",
    }
]

output = {
        "name": "asciified_image",
        "type": "text",
        "example": "asciified_image"
    }

router = APIRouter()

TaskRouter(router=router, input=input, output=output, default_model="ramesh-aditya")
