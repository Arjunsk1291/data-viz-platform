from flask import Blueprint, jsonify
from ..core.data_fetcher import NasaFetcher 

api = Blueprint('api', __name__)

@api.route('/nasa/apod')
def nasa_apod():
    fetcher = NasaFetcher()
    data = fetcher.get_astronomy_picture()
    return jsonify(data)