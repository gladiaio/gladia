
from fastapi import APIRouter

from ai_api_utils.submodules import TaskRouter

router = APIRouter()
TaskRouter(router=router, input="image", output="image", default_model="v1")