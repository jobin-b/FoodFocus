# from . import main
from flask import Blueprint
from database import db, get_user, update_day, insert_day

other = Blueprint('other', __name__)
@other.route('/user/<email>', methods=['GET'])
def user(email):
    return get_user(db, email)

@other.route('/')
def index():
    return 'Hello World!'
