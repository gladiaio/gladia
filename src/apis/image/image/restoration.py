from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

TaskRouter(
    router=router,
    input="image",
    output="image",
    default_model="bringing-old-photos-back-to-life",
)
