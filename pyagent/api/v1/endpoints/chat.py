
from fastapi import APIRouter, HTTPException, Depends
from pyagent.models.chat import PostContentRequest, PostContentResponse
from pyagent.services.gemini_service import GeminiService

router = APIRouter()

@router.post("/post-content")
async def post_message(
    request: PostContentRequest,
    gemini_service: GeminiService = Depends(GeminiService),
) -> PostContentResponse:
    if not request.message:
        raise HTTPException(status_code=400, detail="Message is required.")
    try:
        return gemini_service.respond_to_chat(request.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

