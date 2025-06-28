
from .endpoints import weather, api_reference
from fastapi import APIRouter

router = APIRouter()
router.include_router(weather.router)
router.include_router(api_reference.router)
