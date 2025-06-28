from google.genai import types

def get_weather(location: str) -> str:
    return f"The current temperature in {location} is 20°C."

# Define the function declaration for the model
weather_function = {
    "name": "get_weather",
    "description": "Gets the current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city name, e.g. San Francisco",
            },
        },
        "required": ["location"],
    },
}

weather_function_declaration = types.FunctionDeclaration(**weather_function)

__all__ = ["get_weather", "weather_function_declaration"]