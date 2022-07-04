from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter


inputs = [
    {
        "type": "image",
        "name": "image",
        "default": "Image classification",
        "placeholder": "Image to classify",
        "tooltip": "Image to classify",
    },
    {
        "type": "text",
        "name": "top_k",
        "default": "1",
        "placeholder": "Top K",
        "tooltip": "Top K",
    },
]

output = {"name": "classified_image", "type": "text", "example": "class: probability%"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="resnet50")
