from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "sentence",
        "default": "I think therefore I",
        "placeholder": "I think therefore I",
        "tooltip": "Insert the text to find the next word from.",
    },
]

output = {
        "name": "next_word",
        "type": "str",
        "example": "next word"
    }


TaskRouter(router=router, input=input, output=output, default_model="distilbert-base-uncased")
