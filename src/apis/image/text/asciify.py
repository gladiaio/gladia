from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png",
        "placeholder": "image url to convert to ascii if no file upload",
        "tooltip": "Insert the image to convert to ascii",
    }
]

output = {"name": "asciified_image", "type": "text", "example": "asciified_image"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="ramesh-aditya")
