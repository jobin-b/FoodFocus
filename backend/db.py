import bson

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo

from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime

import os

def init_db():
    db = g._database = PyMongo(current_app).db

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
        
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

def get_user(db, email):
    if db.user.find({"email": email}) is None:
        doc = {
            "_id": email,
            "email": email
        }
        return db.user.insert_one(doc)
    
    return db.user.find({"email": email})


def insert_day(db, meal_data, id, day):
    
    user = get_user(db,id)
    

    doc_day = {
        "user_id" : meal_data["_id"],
        "time" : datetime.now(),
        "totals" : {
            "co2" : meal_data["co2"],
            "calories" : meal_data["calories"],
            "protein": meal_data["protein"],
            "carbohydrates": meal_data["carbohydrates"],
            "fat": meal_data["fat"]
        }
    }

    return db.meals.insert_one(doc_day)

def update_day(db, meal_data, id, day):
    user = get_user(db, id)

    doc_day = {
        "user_id" : meal_data["_id"],
        "time" : datetime.now(),
        "totals" : {
            "co2" : meal_data["co2"] + day["totals"]["co2"],
            "calories" : meal_data["calories"] + day["totals"]["calories"],
            "protein": meal_data["protein"] + day["totals"]["protein"],
            "carbohydrates": meal_data["carbohydrates"] + day["totals"]["carbohydrates"],
            "fat": meal_data["fat"] + day["totals"]["fat"]
        }
    }
    response = db.meals.update_one({"_id": day["_id"]}, {"$set": doc_day})
    return response.json()

def get_meals(db, day_id):
    return db.meals.find({"_id": day_id})

def get_meal(db, meal_id):
    return db.meals.find({"_id": ObjectId(meal_id)})

def get_all_meals(db, user_id):
    return db.meals.find({"user_id": user_id})
    
def delete_meal(db, meal_id):
    return db.meals.delete_one({"_id": ObjectId(meal_id)})
