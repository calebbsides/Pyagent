from typing import List
from pyagent.clients.gemini import get_gemini_client
from google.genai import types
from pyagent.core.config import settings
from pyagent.core.errors import http_500_error
from pyagent.models.chat import ChatMessage

def respond_to_chat(chat_history: List[ChatMessage]) -> str:
    try:
        client = get_gemini_client()
        contents = []

        # Build chat history for Gemini
        # Gemini expects a list of Content objects, each with a role and parts
        # Parts is a list of Part objects, each with text
        if chat_history:
            for msg in chat_history:
                contents.append(types.Content(role=msg.role, parts=[types.Part(text=msg.text)]))

        response = client.models.generate_content(
            model=settings.BASE_MODEL,
            contents=contents
        )

        candidates = getattr(response, "candidates", None)
        if not candidates or not candidates[0] or not hasattr(candidates[0], "content"):
            raise RuntimeError("No response from Gemini.")
            
        content = candidates[0].content
        if not content or not hasattr(content, "parts") or not content.parts or not content.parts[0]:
            raise RuntimeError("No response from Gemini.")
        
        text = getattr(content.parts[0], "text", None)
        if not text:
            raise RuntimeError("No response from Gemini.")
        
        return text
    except Exception as exc:
        raise http_500_error(exc)
