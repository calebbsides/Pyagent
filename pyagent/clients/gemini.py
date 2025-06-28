# Gemini client setup
import os
from google.genai import Client

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set in environment.")
    return Client(api_key=api_key)
