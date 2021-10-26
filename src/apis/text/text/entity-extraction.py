from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "input_string",
        "default": "Text to extract entities from",
        "placeholder": "Text to extract entities from",
        "tooltip": "Insert the text to extract entities from",
    }
]

output = {
        "name": "extracted_entities",
        "type": "list",
        "example": "extracted_entities"
    }


TaskRouter(router=router, input=input, output=output, default_model="dbmdz-bert-large-cased-finetuned-conll03-english")
