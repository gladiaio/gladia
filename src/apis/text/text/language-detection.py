from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "text",
        "default": "Input text to perform language detection on",
        "placeholder": "Input text to perform language detection on",
        "tooltip": "Insert the text to perform language detection on"
    },
]

output = {
        "name": "generated_text",
        "type": "str",
        "example": "generated_text"
    }

TaskRouter(router=router, input=input, output=output, default_model="toftrup-etal-2021")
