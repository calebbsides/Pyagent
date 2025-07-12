from pydantic import BaseModel

class PostContentRequest(BaseModel):
    message: str

class PostContentResponse(BaseModel):
    Facebook: str
    Instagram: str
    LinkedIn: str
    TikTok: str
    YouTube: str
    Snapchat: str
    X: str
    Reddit: str