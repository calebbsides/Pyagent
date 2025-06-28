# Weather function
def get_weather(city: str) -> str:
    """Fetches the current temperature for a given city."""
    # This is a placeholder. Replace with a real API call as needed.
    # Example: response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q={city}")
    # data = response.json()
    # return f"{city}: {data['current']['temp_c']}°C"
    return f"The current temperature in {city} is 20°C."
