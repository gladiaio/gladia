from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "code_snippet",
        "default": "def is_palendrome(s):",
        "placeholder": "Input code to start generation from",
        "tooltip": "Insert the code to generate from",
    },
]

output = {
        "name": "generated_code",
        "type": "str",
        "example": "generated_code"
    }

TaskRouter(router=router, input=input, output=output, default_model="sentdex-GPyT")
