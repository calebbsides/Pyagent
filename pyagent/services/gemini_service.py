import os
from fastapi import HTTPException
from google.genai import types, Client
from dotenv import load_dotenv
from pyagent.tools.facebook_tool import create_fb_post
from pyagent.tools.instagram_tool import create_ig_post

load_dotenv()

class GeminiService:
    _model = "gemini-2.5-flash"
    _config = types.GenerateContentConfig(
        tools=[create_fb_post, create_ig_post],
        system_instruction=(
            "You are a social media influencer assistant."
            "You create engaging, trendy, and relevant social media posts for millions of followers."
            "Use the tools provided to post content to social media."
            "Always use trending hashtags and emojis in your posts."
            "Do not create posts without using the tools."
            "If you are unsure about the platform, post the content to all platforms."
            "Do not respond without using the tools."
        ),
        temperature=0.3
    )

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self._client = Client(api_key=api_key)

    def respond_to_chat(self, prompt: str):
        try:
            response = self._client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt],
                config=self._config,
            )
            return response.text
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Gemini service error: {exc}")