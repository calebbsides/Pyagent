
from .endpoints import weather
from fastapi import APIRouter

router = APIRouter()
router.include_router(weather.router)
