import bson
#from bson import json_util

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from food_classifier import nutr_from_img
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime

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

        return res.inserted_id
    return user


#mealdata = img_file
def insert_day(db, img_filepath, user_id, day_info):
    meal_data = nutr_from_img(img_filepath)
    user = get_user(db,user_id)
    

    doc_day = {
        "user_id" : user["_id"],
        "time" : day_info,
        "totals" : {
            "co2" : meal_data["co2"],
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
            "co2" : meal_data["co2"] + total_day["totals"]["co2"],
            "calories" : meal_data["calories"] + total_day["totals"]["calories"],
            "protein": meal_data["protein"] + total_day["totals"]["protein"],
            "carbohydrates": meal_data["carbohydrates"] + total_day["totals"]["carbohydrates"],
            "fat": meal_data["fat"] + total_day["totals"]["fat"]
        }
    }
    response = db.days.update_one({"_id": total_day["_id"]}, {"$set": doc_day})
    
    return response.json()

# add meal func
# date, userid
# if day doesn't exist make new one else get existing
# create meal and add to day
def add_meal(db,img_filepath,user_id, date):
    meal_data = nutr_from_img(img_filepath)
    day_id = db.days.find({"user_id": user_id, "time": date})['_id']
    if day_id is None:
        res = insert_day(db,meal_data, user_id, date)
        res = res.inserted_id
    else:
        update_today(db,meal_data, user_id, day_id, date)
    response = db.meals.insert_one({
        "user_id": user_id,
        "dayid": day_id,
        "co2" : meal_data["co2"],
        "calories" : meal_data["calories"],
        "protein": meal_data["protein"],
        "carbohydrates": meal_data["carbohydrates"],
        "fat": meal_data["fat"]
    })
    return response.json()



def get_meals_by_day(db, user_id,date):
    day_id =  db.days.find({"user_id": user_id, "time": date})['_id']
    return db.meals.find({"dayid": day_id})

def get_meal(db, meal_id):
    return db.meals.find({"_id": ObjectId(meal_id)})

def get_all_meals(db, user_id):
    return db.meals.find({"user_id": user_id})
    
def delete_meal(db, meal_id):
    return db.meals.delete_one({"_id": ObjectId(meal_id)})

def get_day(db, day_id):
    return db.days.find({"_id": ObjectId(day_id)})

def get_day_from_date(db, user_id, date):
    return db.days.find({"user_id": user_id, "time": date})

def get_macros(db, user_id):
    return db.user.find({"_id": user_id})["macros"]

def update_macros(db, user_id, macros):
    return db.user.update_one({"_id": user_id}, {"$set": {"macros": macros}})
