from google.genai import types

def create_tiktok_post(content: str) -> str:
    print(f"Creating TikTok post with content: {content}")
    return f"Posted to TikTok: {content}"
