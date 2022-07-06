from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "text",
        "default": "Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO, therefore very close to the Manhattan Bridge.",
        "placeholder": "I like you. I love you",
        "tooltip": "Insert the text to anlayse sentiment from",
    }
]

output = {"name": "results", "type": "list", "example": "results"}

TaskRouter(
    router=router,
    input=inputs,
    output=output,
    default_model="dbmdz-bert-large-cased-finetuned-conll03-english",
)
