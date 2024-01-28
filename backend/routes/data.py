# from . import main
from flask import Blueprint, request, jsonify
from database import db, get_user, update_today, insert_day, get_meals_by_day, get_meals_by_day, get_meal, delete_meal, get_day, get_day_from_date, get_macros, update_macros, add_meal
import os
other = Blueprint('other', __name__)
@other.route('/user/<email>', methods=['GET'])
def user(email):
    res = get_user(db, email)
    print(res)
    return res

# @other.route('/nutrients/', methods=['POST'])
# def get_nutrients():
#     print('Get image nutrients')
#     if 'file' not in request.files:
#         return 'No file part'dat
#     image = request.files['file']

#     image_dir = os.path.join("/home/ryan/Desktop/imageUpload",image.filename)
#     image.save(image_dir)

#     return get_nutrients(image)


@other.route('/day_in/', methods=['POST', 'UPDATE'])
def insert_or_update():
    if 'file' not in request.files:
        return "No file part"
    image = request.files['file']
    print("CHECK")

    print(image)
    current_folder = os.path.join("/home/ryan/Desktop/imageUpload",image.filename)
    image.save(current_folder)

    image_path = current_folder


    user_id = request.form['user_id']
    day_info = request.form['day']
    print(day_info)

    if request.method == 'UPDATE':
        tot_day = request.form['curr_day']
        return add_meal(db, image_path, user_id, tot_day, day_info)
    else:
        return add_meal(db, image_path, user_id, day_info)


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
    print('Query day for user ' + user_id + " date" + date)
    return get_day_from_date(db, user_id, date)

@other.route('/macros/<user_id>/', methods=['GET', 'POST'])
def obtain_macros(user_id):
    if request.method == 'GET':
        return get_macros(db, user_id)  
    else:
        json = request.get_json()
        calories = ['calories']
        protein = json['protein']
        carbs = json['carbohydrates']
        fat = json['fat']
        print(calories, protein, carbs, fat)
        macros = {
            'calories': calories,
            'protein': protein,
            'carbohydrates': carbs,
            'fat': fat
        }
        update_macros(db, user_id, macros)
        return 'success'

@other.route('/')
def index():
    return 'Hello World!'

