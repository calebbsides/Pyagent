from typing import List
from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    text: str

class PostMessageRequest(BaseModel):
    chat_history: List[ChatMessage]
