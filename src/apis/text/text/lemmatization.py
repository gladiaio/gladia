from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "sentence",
        "default": "My name is Clara and I live in Berkeley.",
        "placeholder": "My name is Clara and I live in Berkeley.",
        "tooltip": "Insert the text to do lemmatization on",
    },
]

output = {
        "name": "lemmatized_text",
        "type": "str",
        "example": "lemmatized_text"
    }


TaskRouter(router=router, input=input, output=output, default_model="wordnet")
