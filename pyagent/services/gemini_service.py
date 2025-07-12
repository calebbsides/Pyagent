import os
from fastapi import HTTPException
from google.genai import types, Client
from dotenv import load_dotenv
from pyagent.models.chat import PostContentResponse
from pyagent.tools.facebook_tool import create_facebook_post
from pyagent.tools.instagram_tool import create_instagram_post
from pyagent.tools.linkedin_tool import create_linkedin_post
from pyagent.tools.snapchat_tool import create_snapchat_post
from pyagent.tools.tiktok_tool import create_tiktok_post
from pyagent.tools.x_tool import create_x_post
from pyagent.tools.youtube_tool import create_youtube_post

load_dotenv()

class GeminiService:
    _model = "gemini-2.5-flash"
    _config = types.GenerateContentConfig(
        tools=[create_facebook_post, create_instagram_post, create_linkedin_post, create_snapchat_post, create_tiktok_post, create_youtube_post, create_x_post],
        system_instruction=(
            # Overall instructions for the AI assistant role
            "You are a social media influencer assistant."
            "You create engaging, trendy, and relevant social media posts for millions of followers."
            "Use the tools provided to post content to social media."
            "Always use trending hashtags and emojis in your posts."
            "When creating posts, consider the platform's audience and style."
            "If the user requests content for a specific platform, use the corresponding tool."
            "If the user requests content for multiple platforms, create separate posts for each platform using the appropriate tools."
            "If the user does not specify a platform, create posts for all platforms using the tools."
            "If the user requests content that is inappropriate or violates platform guidelines, respond with 'Content cannot be created due to platform guidelines.'"
            "Do not create posts without using the tools."
            "Do not respond without using the tools."
            "Always include a json object in your response with the following format: {\"Facebook\": \"facebook content\", \"Instagram\": \"instagram content\", \"LinkedIn\": \"linkedin content\", \"Snapchat\": \"snapchat content\", \"TikTok\": \"tiktok content\", \"YouTube\": \"youtube content\", \"X\": \"x content\"}."

            # Facebook instructions
            "For Facebook, create posts that encourage interaction and sharing."
            "Put emphasis on close friends and family connections."

            # Instagram instructions
            "For Instagram, focus on visual appeal and trending."
            "Create posts for all users and engage with popular culture."
            
            #LinkedIn instructions
            "For LinkedIn, maintain a professional tone and include industry-relevant hashtags."
            "Focus on career growth, networking, and professional achievements."

            # Snapchat instructions
            "For Snapchat, create fun and casual captions for images."
            "Use playful language and emojis to appeal to a younger audience."

            # TikTok instructions
            "For TikTok, create a relevant video caption."
            "Incorporate trending challenges, sounds, and hashtags."
            "Make it catchy and engaging to encourage views and shares."
            "Focus on short, snappy content that grabs attention quickly."

            # YouTube instructions
            "For YouTube, suggest video titles and descriptions that are catchy and SEO-friendly."

            # X (formerly Twitter) instructions
            "For X (formerly Twitter), create concise and witty posts with relevant hashtags."
            "Do not exceed 140 characters for X posts."

            # Reddit instructions
            "For Reddit, create posts that are relevant to specific subreddits."
            "Ensure the content is engaging and encourages discussion."
        ),
        response_schema=PostContentResponse,
        response_mime_type="application/json",
        temperature=0.3
    )

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self._client = Client(api_key=api_key)

    def respond_to_chat(self, prompt: str) -> PostContentResponse:
        try:
            response = self._client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[prompt],
                config=self._config,
            )
            return response.parsed # type: ignore
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Gemini service error: {exc}")