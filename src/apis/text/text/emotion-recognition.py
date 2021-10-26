from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter
from pydantic import BaseModel

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "text",
        "default": "I like you. I love you",
        "placeholder": "I like you. I love you",
        "tooltip": "Insert the text to anlayse sentiment from",
    },
]

output = {
        "name": "results",
        "type": "str",
        "example": "results"
    }

TaskRouter(router=router, input=input, output=output, default_model="mrm8488-t5-base-finetuned-emotion")
