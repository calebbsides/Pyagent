
from .endpoints import chat as post_message
from fastapi import APIRouter

router = APIRouter()
router.include_router(post_message.router)
