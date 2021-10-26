from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "sentence",
        "default": "Once, a group of frogs was roaming around the forest in search of water.",
        "placeholder": "Once, a group of frogs was roaming around the forest in search of water.",
        "tooltip": "Insert the sentence to perform the Pairwise Sentence Scoring Tasks",
    },
]

output = {
        "name": "analyzed_sentence",
        "type": "str",
        "example": "analyzed_sentence"
    }

TaskRouter(router=router, input=input, output=output, default_model="UKPLab-all-MiniLM-L6-v2")
