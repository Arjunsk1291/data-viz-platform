# src/core/stock_fetcher.py
import requests
from src.config import Config

class StockFetcher:
    def get_stock_data(self, symbol: str) -> dict:
        try:
            response = requests.get(
                Config.STOCK_BASE_URL,
                params={
                    'function': 'TIME_SERIES_DAILY',
                    'symbol': symbol,
                    'apikey': Config.STOCK_API_KEY
                }
            )
            data = response.json()
            time_series = data['Time Series (Daily)']
            return {
                'latest': list(time_series.values())[0],
                'historical': time_series
            }
        except Exception as e:
            return {'error': str(e)}