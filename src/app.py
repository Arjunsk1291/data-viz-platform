import sys
from pathlib import Path
from flask import Flask, render_template
from src.api.routes import api

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

app = Flask(__name__,
            template_folder="../frontend/templates",
            static_folder="../frontend/static")

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)