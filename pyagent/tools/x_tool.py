from google.genai import types

def create_x_post(content: str) -> str:
    print(f"Creating X post with content: {content}")
    return f"Posted to X: {content}"
