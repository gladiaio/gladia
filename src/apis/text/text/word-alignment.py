from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "input_string_language_1",
        "default": "Sentence from first language",
        "placeholder": "Sentence from first language",
        "tooltip": "Insert the Sentence from first language",
    },
    {
        "type": "text",
        "name": "input_string_language_2",
        "default": "来自 第一 语言的 句子",
        "placeholder": "来自 第一 语言的 句子",
        "tooltip": "Insert the Sentence from second language",
    },
]

output = {
        "name": "word_aligment",
        "type": "dict",
        "example": "word_aligment"
    }

TaskRouter(router=router, input=input, output=output, default_model="bert-base-multilingual-cased")
