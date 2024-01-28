
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os



app = Flask(__name__)
CORS(app)
load_dotenv('env/.env')

app.config['DEBUG'] = True
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

from database import get_db

with app.app_context():
    db = get_db()

# Import routes
from routes.data import other
app.register_blueprint(other)
if __name__ == '__main__':
    app.run()

