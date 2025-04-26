import sys
from pathlib import Path
from flask import Flask, render_template
from src.extensions import limiter, cache  
from src.extensions import limiter  # Changed import

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")

# Initialize limiter with Redis storage (optional)
limiter.init_app(app)
cache.init_app(app)
limiter.storage_uri = "memory://"  # Simple in-memory storage

# Import routes AFTER initializing limiter
from src.api.routes import api

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)