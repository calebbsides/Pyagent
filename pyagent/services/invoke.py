from pyagent.tools.weather import get_weather

def invoke(name: str, args: dict) -> str:
    """Invoke a registered function by name with provided arguments."""
    if name == "get_weather":
        if isinstance(args, dict):
            return get_weather(**args)
        return get_weather(*args)
    return f"Unknown function: {name}"
