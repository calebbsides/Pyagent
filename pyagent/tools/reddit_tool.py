from google.genai import types

def create_reddit_post(content: str) -> str:
    print(f"Creating Reddit post with content: {content}")
    return f"Posted to Reddit: {content}"
