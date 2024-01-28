# from . import main
from flask import Blueprint, request, jsonify
from database import db, get_user, update_today, insert_day, get_meals_by_day, get_meals_by_day, get_meal, delete_meal, get_day, get_day_from_date, get_macros, update_macros

other = Blueprint('other', __name__)
@other.route('/user/<email>', methods=['GET'])
def user(email):
    res = get_user(db, email)
    print(res)
    return res

@other.route('/day_in/', methods=['POST', 'UPDATE'])
def insert_or_update():
    print("HI!!!!")
    img_path = request.form['img_path']
    user_id = request.form['user_id']
    day_info = request.form['day']

    if request.method == 'UPDATE':
        tot_day = request.form['curr_day']
        return update_today(db, img_path, user_id, tot_day, day_info)
    
    else:
        return insert_day(db, img_path, user_id, day_info)


@other.route('/meals/<user_id>/<date>', methods=['GET'])
def obtain_meals(user_id, date):
    return get_meals_by_day(db, user_id, date)
    

@other.route('/allmeals/<meal_id>', methods=['GET','DELETE'])
def obtain_meal(meal_id):
    if request.method == 'GET':
        return get_meal(db, meal_id)
    else:
        return delete_meal(db, meal_id)

@other.route('/day/<day_id>, methods=[GET]')
def obtain_day(day_id):
    return get_day(db, day_id)


@other.route('/day_from_date/<user_id>/<date>', methods=['GET'])
def obtain_day_from_date(user_id, date):
    return get_day_from_date(db, user_id, date)

@other.route('/macros/<user_id>/', methods=['GET', 'PUT'])
def obtain_macros(user_id):
    if request.method == 'GET':
        return get_macros(db, user_id)  
    else:
        calories = request.body['calories']
        protein = request.body['protein']
        carbs = request.body['carbohydrates']
        fat = request.body['fat']
        macros = {calories, protein, carbs, fat}
        return update_macros(db, user_id, macros)

@other.route('/')
def index():
    return 'Hello World!'

