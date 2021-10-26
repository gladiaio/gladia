from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "sentence",
        "default": "Text to corrcte",
        "placeholder": "Text to corrcte",
        "tooltip": "Insert the text to correct here",
    }
]

output = {
        "name": "corrected_text",
        "type": "str",
        "example": "corrected_text"
    }

TaskRouter(router=router, input=input, output=output, default_model="flexudy-t5-base-multi-sentence-doctor")
