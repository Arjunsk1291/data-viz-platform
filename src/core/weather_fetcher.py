# src/core/weather_fetcher.py
import requests
from src.config import Config

class WeatherFetcher:
    def get_weather(self, city: str) -> dict:
        try:
            response = requests.get(
                Config.WEATHER_BASE_URL,
                params={
                    'q': city,
                    'appid': Config.WEATHER_API_KEY,
                    'units': 'metric'
                }
            )
            data = response.json()
            return {
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }
        except Exception as e:
            return {'error': str(e)}