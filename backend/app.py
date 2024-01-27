from flask import Flask, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os
app = Flask(__name__)
CORS(app)
load_dotenv('env/.env')
key = os.getenv('KEY')
print(key)

@app.route('/')
def hello_world():
    return 'Jobin!!'

@app.route('/api')
def api():
    response = requests.get(f'https://api.edamam.com/api/nutrition-data?app_id=8997459b&app_key={key}&nutrition-type=logging&ingr=hamburger')
    return jsonify(response.json())