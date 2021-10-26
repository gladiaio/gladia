from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "text",
        "default": "Лорем ипсум долор сит амет",
         "tooltip": "Insert the text to transliterate here",
    },
    {
        "type": "text",
        "name": "language",
        "default": "ru",
        "tooltip": "Insert the language code here",
    },
]

output = {
        "name": "transliterated_text",
        "type": "str",
        "example": "transliterated_text"
    }

TaskRouter(router=router, input=input, output=output, default_model="transliterate")
