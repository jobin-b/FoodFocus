import bson
#from bson import json_util

from flask import current_app, g, jsonify
import json
from json import JSONEncoder
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from food_classifier import nutr_from_img
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime
from bson import json_util

import os

# def init_db():
#     db = g._database = PyMongo(current_app).db

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
    
    #print(db is None or db)
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

def get_user(db, email):
    user = db.user.find_one({"email": email})
    if user is None:
        doc = {
            "_id": email,
            "email": email,
            "macros":
            {"calories": 2000,
            "protein": 150,
            "carbohydrates": 200,
            "fat": 67,}
        }
        
        res = db.user.insert_one(doc)

        return doc
    return user


def insert_day(db, meal_data, user_id, day_info):
    user = get_user(db,user_id)

    doc_day = {
        "user_id" : user["_id"],
        "time" : day_info,
        "totals" : {
            "co2" : meal_data["carbon"],
            "calories" : meal_data["calories"],
            "protein": meal_data["protein"],
            "carbohydrates": meal_data["carbohydrates"],
            "fat": meal_data["fat"]
        }
    }

    if db.days.insert_one(doc_day) is not None:
        return doc_day
    else:
        return None
    

def get_today(db,day_id):
    return db.days.find({"_id": ObjectId(day_id)})

def update_today(db, meal_data, id, total_day, day_info):

    
    user = get_user(db, id)

    doc_day = {
        "user_id": user["_id"],
        "time" : day_info,
        "totals" : {
            "co2" : meal_data["carbon"] + total_day["totals"]["co2"],
            "calories" : meal_data["calories"] + total_day["totals"]["calories"],
            "protein": meal_data["protein"] + total_day["totals"]["protein"],
            "carbohydrates": meal_data["carbohydrates"] + total_day["totals"]["carbohydrates"],
            "fat": meal_data["fat"] + total_day["totals"]["fat"]
        }
    }
    response = db.days.update_one({"_id": total_day["_id"]}, {"$set": doc_day})
    
    return doc_day

# add meal func
# date, userid
# if day doesn't exist make new one else get existing
# create meal and add to day
def add_meal(db,img_filepath,user_id, date):
    meal_data = nutr_from_img(img_filepath)
    # day_id = db.days.find_one({"user_id": user_id, "time": date})['_id']
    day_real = db.days.find_one({"user_id": user_id, "time": date})
    if day_real is None:
        day_real = insert_day(db,meal_data, user_id, date)
    else:
        update_today(db,meal_data, user_id, day_real, date)
    response = db.meals.insert_one({
        "user_id": user_id,
        "dayid": day_real["_id"],
        "co2" : meal_data["carbon"],
        "calories" : meal_data["calories"],
        "protein": meal_data["protein"],
        "carbohydrates": meal_data["carbohydrates"],
        "fat": meal_data["fat"]
    })

    return "hi"



def get_meals_by_day(db, user_id,date):
    day =  db.days.find({"user_id": user_id, "time": date})

    if(day is None):
        return None
    
    
    return db.meals.find({"dayid": day['_id']})

def get_meal(db, meal_id):
    return db.meals.find_one({"_id": ObjectId(meal_id)})

def get_all_meals(db, user_id):
    return db.meals.find({"user_id": user_id})
    
def delete_meal(db, meal_id):
    return db.meals.delete_one({"_id": ObjectId(meal_id)})

def get_day(db, day_id):
    return db.days.find_one({"_id": ObjectId(day_id)})


def get_day_from_date(db, user_id, date):
    return db.days.find_one({"user_id": user_id, "time": date})

def get_macros(db, user_id):
    return db.user.find_one({"_id": user_id})["macros"]

def update_macros(db, user_id, macros):
    return db.user.update_one({"_id": user_id}, {"$set": {"macros": macros}})
