from pyagent.services.invoke import invoke
from google.genai import types

def handle_function_calls(function_calls: list[types.FunctionCall], contents: list[types.Content]) -> list[types.Content]:
    """
    Handle function calls from Gemini response and update contents with function responses.
    """
    for function_call in function_calls:
        name = getattr(function_call, "name", None)
        args = getattr(function_call, "args", None)
        if not name or not args:
            continue
        result = invoke(name, args)
        function_response_part = types.Part.from_function_response(
            name=name,
            response={"result": result},
        )
        contents.append(types.Content(role="user", parts=[function_response_part]))
    return contents
