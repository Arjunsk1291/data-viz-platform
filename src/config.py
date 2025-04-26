import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from project root
BASE_DIR = Path(__file__).resolve().parent.parent  # Points to project root
load_dotenv(BASE_DIR / '.env')

class Config:
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    DEBUG = os.getenv("DEBUG", False)