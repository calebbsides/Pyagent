from pyagent.clients.gemini import get_gemini_client
from pyagent.tools.tools import tools
from google.genai import types
from pyagent.utils.function_calls import handle_function_calls
from pyagent.core.config import settings
from pyagent.core.errors import http_500_error

def generate_weather_content():
    """
    Generate weather content for London using Gemini and a function call tool.
    """
    client = get_gemini_client()
    prompt = "What's the temperature in London?"
    config = types.GenerateContentConfig(tools=tools)
    contents = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    try:
        response = client.models.generate_content(
            model=settings.BASE_MODEL,
            contents=contents,
            config=config,
        )
        function_calls = getattr(response, "function_calls", None)
        if function_calls:
            contents = handle_function_calls(function_calls, contents)
        final_response = client.models.generate_content(
            model=settings.BASE_MODEL,
            config=config,
            contents=contents,
        )
        return getattr(final_response, "text", final_response)
    except Exception as exc:
        raise http_500_error(exc)
