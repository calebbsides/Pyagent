# Tool registration
from google.genai import types

tools = [
    types.FunctionDeclaration(
        parameters=None  # No schema, simple string argument for demo
    )
]
