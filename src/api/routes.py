from flask import Blueprint, jsonify  # Add Blueprint here
from src.extensions import limiter, cache
from src.core.data_fetcher import NasaFetcher
from src.core.weather_fetcher import WeatherFetcher
from src.core.stock_fetcher import StockFetcher

api = Blueprint('api', __name__) 

# Static route first
@api.route('/nasa/apod')
@limiter.limit("10/minute")
def nasa_apod():
    return jsonify(NasaFetcher().get_astronomy_picture())

# Parameterized routes after
@api.route('/weather/<string:city>')
@limiter.limit("15/minute")
def get_weather(city: str):
    if not city.replace(" ", "").isalpha():
        return jsonify({"error": "Invalid city name"}), 400
    return jsonify(WeatherFetcher().get_weather(city))

@api.route('/stocks/<string:symbol>')
@cache.cached(timeout=300)
def get_stock(symbol: str):
    return jsonify(StockFetcher().get_stock_data(symbol))