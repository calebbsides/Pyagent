from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: str
    text: str

class PostMessageRequest(BaseModel):
    message: str
