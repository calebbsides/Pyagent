
"""
tools
-------
This module provides the tool declarations for use with the Google GenAI API.
"""

from google.genai import types
from tools.weather_function import weather_function_declaration

tools = types.Tool(function_declarations=[weather_function_declaration])

__all__ = ["tools"]