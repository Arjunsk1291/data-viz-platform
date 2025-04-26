import requests
from ..config import Config  # Relative import

class NasaFetcher:
    def get_astronomy_picture(self):
        """Get NASA's Astronomy Picture of the Day"""
        try:
            response = requests.get(
                "https://api.nasa.gov/planetary/apod",
                params={'api_key': Config.NASA_API_KEY}
            )
            return response.json()
        except Exception as e:
            print(f"Error: {str(e)}")
            return None