import os
from dotenv import load_dotenv
from fastapi import HTTPException
from google import genai

load_dotenv()

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=400, detail=f"GEMINI_API_KEY environment variable is not set: {str(api_key)}")
    try:
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize GenAI client: {str(e)}")
    
__all__ = ["get_gemini_client"]