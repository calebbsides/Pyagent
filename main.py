import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

BASE_MODEL = "gemini-2.0-flash"

# Load environment variables from .env file
load_dotenv()
app = FastAPI()

class GenerateContentRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

def get_genai_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=400, detail=f"GEMINI_API_KEY environment variable is not set: {str(api_key)}")
    try:
        # The client gets the API key from the environment variable `GEMINI_API_KEY`.
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize GenAI client: {str(e)}")
    
@app.post("/generate-content")
async def generate_content(request: GenerateContentRequest):
    client = get_genai_client()
    try:
        response = client.models.generate_content(
            model=BASE_MODEL, 
            contents=request.prompt
        )
        return {"generated_text": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")