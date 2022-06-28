from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "sentence_1",
        "default": "",
        "placeholder": "I like Python because I can do data analytics",
        "tooltip": "Insert the text to compare here",
    },
    {
        "type": "text",
        "name": "sentence_2",
        "default": "",
        "placeholder": "Second sentence to compare to",
        "tooltip": "Insert the text to compare here",
    },
]

output = {
        "name": "similarity",
        "type": "float",
        "example": "similarity"
    }

TaskRouter(router=router, input=inputs, output=output, default_model="all-MiniLM-L6-v2")
