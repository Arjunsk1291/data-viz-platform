from flask import Blueprint, jsonify
from ..core.data_fetcher import NasaFetcher 
from ..core.weather_fetcher import WeatherFetcher
from ..core.stock_fetcher import StockFetcher

api = Blueprint('api', __name__)

@api.route('/nasa/apod')

@api.route('/weather/<city>')
@limiter.limit("10/minute") 

def get_weather(city):
    if not city.isalpha():
        return jsonify({'error': 'Invalid city name'}), 400
    fetcher = WeatherFetcher()
    return jsonify(fetcher.get_weather(city))


def nasa_apod():
    fetcher = NasaFetcher()
    data = fetcher.get_astronomy_picture()
    return jsonify(data)

@api.route('/stocks/<symbol>')
@cache.cached(timeout=300)
def get_stock(symbol):
    fetcher = StockFetcher()
    return jsonify(fetcher.get_stock_data(symbol))

