from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png",
        "placeholder": "Image to colorize",
        "tooltip": "Image to colorize",
    }
]

output = {"name": "colorized_image", "type": "image", "example": "image"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="deoldify-stable")
