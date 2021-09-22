from fastapi import APIRouter
from ai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "sentence_1",
        "default": "I like Python because I can build AI applications",
        "placeholder": "I like Python because I can do data analytics",
        "tooltip": "Insert the text to compare here",
    },
    {
        "type": "text",
        "name": "sentence_2",
        "default": "Second sentence to compare to",
        "placeholder": "Second sentence to compare to",
        "tooltip": "Insert the text to compare here",
    },
]

output = [
    {
        "type": float,
        "name": "similarity",
    }
]

TaskRouter(router=router, input=input, output=output, default_model="all-MiniLM-L6-v2")
