from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "input_string",
        "default": "Text to analyzed",
        "placeholder": "Text to analyzed",
        "tooltip": "Insert the text to analyzed here",
    }
]

output = {"name": "analyzed_text", "type": "str", "example": "analyzed_text"}


TaskRouter(router=router, input=inputs, output=output, default_model="LAL-Parser")
