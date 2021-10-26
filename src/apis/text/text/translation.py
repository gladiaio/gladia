from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "input_string",
        "default": "Text to translate",
        "placeholder": "Text to translate",
        "tooltip": "Insert the text to translate here",
    },
    {
        "type": "text",
        "name": "source_language",
        "default": "en",
        "tooltip": "Please use the ISO 2 letters representation for source language",
    },
    {
        "type": "text",
        "name": "target_language",
        "default": "fr",
        "tooltip": "Please use the ISO 2 letters representation for target language",
    },
]

output = {
        "name": "translated_text",
        "type": "str",
        "example": "translated_text"
    }

TaskRouter(router=router, input=input, output=output, default_model="Helsinki-NLP")
