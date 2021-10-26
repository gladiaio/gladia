from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "input_string",
        "default": "Text to analyzed",
        "placeholder": "Text to analyzed",
        "tooltip": "Insert the text to analyzed here",
    },
]

output = {
        "name": "analyzed_text",
        "type": "str",
        "example": "analyzed_text"
    }


TaskRouter(router=router, input=input, output=output, default_model="LAL-Parser")
