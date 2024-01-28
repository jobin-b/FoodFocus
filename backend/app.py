from flask import Flask, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
from db import get_db, init_db
import os

app = Flask(__name__)
CORS(app)
load_dotenv('env/.env')

app.config['DEBUG'] = True
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

with app.app_context():
    db = get_db()

MONGO_URI = os.getenv('MONGO_URI')
EDAMAME_KEY = os.getenv('KEY')


@app.route('/')
def hello_world():
    return 'Jobin!!'

