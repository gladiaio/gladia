from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "sentence",
        "default": "I think therefore I",
        "placeholder": "I think therefore I",
        "tooltip": "Insert the text to find the next word from.",
    }
]

output = {"name": "next_word", "type": "str", "example": "next word"}


TaskRouter(
    router=router, input=inputs, output=output, default_model="distilbert-base-uncased"
)
