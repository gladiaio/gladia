from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "text",
        "default": "I hate you piece of shit",
        "placeholder": "I hate you piece of shit",
        "tooltip": "Insert the text to classify as hate or not",
    }
]

output = {"name": "classified_text", "type": "str", "example": "offensive"}

TaskRouter(
    router=router,
    input=inputs,
    output=output,
    default_model="Hate-speech-CNERG-dehatebert-mono-english",
)
