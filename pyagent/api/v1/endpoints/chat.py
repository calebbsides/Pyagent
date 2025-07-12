
from fastapi import APIRouter, HTTPException
from pyagent.models.chat import PostMessageRequest
from pyagent.services.gemini_service import respond_to_chat

router = APIRouter()

@router.post("/messages")
async def post_message(data: PostMessageRequest):
    if not data.chat_history:
        raise HTTPException(status_code=400, detail="Chat history required.")
    try:
        response = respond_to_chat(data.chat_history)
        return {"text": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

