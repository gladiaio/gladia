from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "audio",
        "name": "audio",
        "default": "https://anshe.org/audio/3Weeks-080715.mp3",
        "placeholder": "Image to transcribe",
        "tooltip": "Image to transcribe",
    },
    {
        "type": "text",
        "name": "language",
        "default": "en",
        "placeholder": "Language",
        "tooltip": "Language",
    },
]

output = {
    "name": "transcription",
    "type": "text",
    "example": "I'm telling you that this is the tools i've seen so far.",
}

router = APIRouter()

TaskRouter(
    router=router, input=inputs, output=output, default_model="coqui_english_huge_vocab"
)
