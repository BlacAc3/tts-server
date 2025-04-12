from flask import Flask
from routes import register_routes
from config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Create required directories
    for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER']]:
        os.makedirs(folder, exist_ok=True)

    # Register all routes
    register_routes(app)

    return app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['DEBUG'],
            host=app.config['HOST'],
            port=app.config['PORT'])
