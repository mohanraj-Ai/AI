from langchain_core.tools import tool
import requests


@tool
def weather(city: str) -> str:
    """
    Get the current weather for a city.
    Example: weather("Chennai")
    """

    try:
        # Step 1: Find city coordinates
        geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

        geocode_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geocode_url,
            params=geocode_params,
            timeout=10
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"City not found: {city}"

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "")

        # Step 2: Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "precipitation,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "temperature_unit": "celsius",
            "wind_speed_unit": "kmh"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]

        return (
            f"Weather for {city_name}, {country}\n"
            f"Temperature: {current['temperature_2m']} °C\n"
            f"Feels like: {current['apparent_temperature']} °C\n"
            f"Humidity: {current['relative_humidity_2m']}%\n"
            f"Precipitation: {current['precipitation']} mm\n"
            f"Wind speed: {current['wind_speed_10m']} km/h\n"
            f"Weather code: {current['weather_code']}"
        )

    except Exception as e:
        return f"Weather API error: {str(e)}"