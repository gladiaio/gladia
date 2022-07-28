from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/1200px-Image_created_with_a_mobile_phone.png",
        "placeholder": "Image to extract text from",
        "tooltip": "Insert the image to extract text from",
    },
    {
        "type": "text",
        "name": "source_language",
        "default": "en",
        "tooltip": "Please use the ISO 2 letters representation for source language",
    },
]

output = {"name": "extracted_text", "type": "list", "example": "extracted_text"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="easy-ocr")
