from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "text",
        "default": "def is_palendrome(s):",
        "placeholder": "Input code to get programing language from",
        "tooltip": "Input code to get programing language from",
    }
]

output = {"name": "classified_code", "type": "list", "example": "classified_code"}

TaskRouter(router=router, input=inputs, output=output, default_model="aliostad")
