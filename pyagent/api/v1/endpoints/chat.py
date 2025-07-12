
from fastapi import APIRouter, HTTPException, Depends
from pyagent.models.chat import PostMessageRequest
from pyagent.services.gemini_service import GeminiService

router = APIRouter()

@router.post("/post-content")
async def post_message(
    request: PostMessageRequest,
    gemini_service: GeminiService = Depends(GeminiService),
):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message is required.")
    try:
        response = gemini_service.respond_to_chat(request.message)
        return {
            "text": response,
            "role": "model"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

