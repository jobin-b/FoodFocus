from flask import Flask, jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Jobin!!'

@app.route('/api')
def api():
    response = requests.get('https://api.edamam.com/api/nutrition-data?app_id=8997459b&app_key=ecdd45aebacc6cc3783c8a2960bb7b50&nutrition-type=logging&ingr=hamburger')
    return jsonify(response.json())