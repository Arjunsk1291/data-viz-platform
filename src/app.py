import sys
from pathlib import Path
from flask import Flask, render_template
from src.api.routes import api
from flask_caching import Cache

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
cache = Cache(config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})
cache.init_app(app)

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

