import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google.genai import types
from clients.gemini import get_gemini_client
from tools.tools import tools
from tools.weather_function import get_weather

BASE_MODEL = "gemini-2.5-flash"

def invoke(name: str, args: dict) -> str:
   if name == "get_weather":
       return get_weather(*args)
   return "Unknown function"


# Load environment variables from .env file
load_dotenv()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Healthy"}

@app.get("/weather")
async def generate_content():
    client = get_gemini_client()
    prompt = "What's the temperature in London?"
    config = types.GenerateContentConfig(tools=[tools])

    # Define user prompt
    contents = [
        types.Content(
            role="user", parts=[types.Part(text=prompt)]
        )
    ]

    try:
        response = client.models.generate_content(
            model=BASE_MODEL,
            contents=contents,
            config=config,
        )

        # Handle function calls if present
        if hasattr(response, "function_calls") and response.function_calls:
            for function_call in response.function_calls:
                name = getattr(function_call, "name", "")
                args = getattr(function_call, "args", {})
                if name:
                    result = invoke(name, args)

                    function_response_part = types.Part.from_function_response(
                        name=name,
                        response={"result": result},
                    )
                    # Add the function response as a new part for the model
                    contents.append(types.Content(role="user", parts=[function_response_part]))

            # Generate a final response after function call(s)
            final_response = client.models.generate_content(
                model=BASE_MODEL,
                config=config,
                contents=contents,
            )
            return final_response.text
        else:
            # No function call, just return the model's response
            return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")