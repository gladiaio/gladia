from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "text",
        "default": "I lSachin Ramesh Tendulkar is a former international cricketer from India and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in International cricket.",
        "placeholder": "I lSachin Ramesh Tendulkar is a former international cricketer from India and a former captain of the Indian national team. He is widely regarded as one of the greatest batsmen in the history of cricket. He is the highest run scorer of all time in International cricket.",
        "tooltip": "Insert the text to generate question",
    }
]

output = {"name": "results", "type": "list", "example": "result"}

TaskRouter(router=router, input=inputs, output=output, default_model="questgen")
