
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from db import get_db

def create_app():
    app = Flask(__name__)
    CORS(app)
    load_dotenv('env/.env')

    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')

    with app.app_context():
        db = get_db()

    # Import routes
    from . import routes

    return app

