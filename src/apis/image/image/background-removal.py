from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png",
        "placeholder": "Image to background removal",
        "tooltip": "Image to background removal",
    }
]

output = {"name": "cleaned_image", "type": "image", "example": "a.png"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="xception")
