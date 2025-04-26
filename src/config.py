import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
BASE_DIR = Path(__file__).resolve().parent.parent  # Points to project root
load_dotenv(BASE_DIR / '.env')

class Config:
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    DEBUG = os.getenv("DEBUG", False)
    WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_KEY")
    STOCK_BASE_URL = "https://www.alphavantage.co/query"