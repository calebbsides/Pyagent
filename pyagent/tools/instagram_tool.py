from google.genai import types

def create_ig_post(content: str) -> str:
    print(f"Creating Instagram post with content: {content}")
    return f"Posted to Instagram: {content}"
