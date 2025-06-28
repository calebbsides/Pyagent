# Tool registration
from google.genai import types

tools = [
    types.FunctionDeclaration(
        name="get_weather",
        description="Get the weather for a given city.",
        parameters=None  # No schema, simple string argument for demo
    )
]
