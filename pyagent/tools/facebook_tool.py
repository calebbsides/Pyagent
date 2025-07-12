from google.genai import types

def create_fb_post(content: str) -> str:
    print(f"Creating Facebook post with content: {content}")
    return f"Posted to Facebook: {content}"
