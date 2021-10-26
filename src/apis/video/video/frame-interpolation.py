from fastapi import APIRouter
from unifai_api_utils.submodules import TaskRouter

input = [
    {
        "type": "video",
        "name": "video",
        "default": "video to interpolate",
        "placeholder": "video to interpolate",
        "tooltip": "video to interpolate"
    }
]

output = {
        "name": "interpolated_video",
        "type": "video",
        "example": "interpolated_video"
    }

router = APIRouter()

TaskRouter(
    router=router,
    input=input,
    output=output,
    default_model="deep-animation-video-interpolation-in-the-wild",
)
