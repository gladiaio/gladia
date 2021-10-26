from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from unifai_api_utils.submodules import TaskRouter

input = [
    {
        "type": "image",
        "name": "image",
        "default": "Image to colorize",
        "placeholder": "Image to colorize",
        "tooltip": "Image to colorize"
    }
]

output = {
        "name": "colorized_image",
        "type": "image",
        "example": "image"
    }

router = APIRouter()

TaskRouter(
    router=router, input=input, output=output, default_model="deoldify-stable"
)
