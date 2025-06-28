from fastapi import APIRouter
from pyagent.services.gemini_service import generate_weather_content

router = APIRouter()

@router.get("/weather")
async def get_weather():
    return generate_weather_content()
