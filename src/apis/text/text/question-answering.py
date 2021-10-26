from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "context",
        "default": "My name is Clara and I live in Berkeley.",
        "placeholder": "Context to extract answer from",
        "tooltip": "Insert the text to extract answer from",
    },
    {
        "type": "text",
        "name": "question",
        "default": "What's my name?",
        "tooltip": "Insert the question to be answered",
    },
]

output = {
        "name": "answer",
        "type": "str",
        "example": "answer"
    }


TaskRouter(router=router, input=input, output=output, default_model="deepset_bert-base-cased-squad2")
