# TF2 version
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
import cv2
from skimage import io
import os
import requests
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
load_dotenv('env/.env')

EDAMAME_KEY = os.getenv('KEY')

root_dir = os.path.dirname(__file__)
labelmap_dir = os.path.join(root_dir, "model/aiy_food_V1_labelmap.csv")
model_dir = os.path.join(root_dir, "model/")
# images_dir = os.path.

model = hub.KerasLayer(model_dir)

test_url = "https://d3mvlb3hz2g78.cloudfront.net/wp-content/uploads/2014/06/thumb_720_450_dreamstime_xl_34122178-Custom.jpg"
input_shape = (224, 224)

# Food classification model from https://www.kaggle.com/models/google/aiy/frameworks/tensorFlow1/variations/vision-classifier-food-v1


model_label_map_classes = list(pd.read_csv(labelmap_dir)["name"])
def predict_image(image_path):
    print("IMAGE_PATH", image_path)
    image = np.asarray(io.imread(image_path), dtype="float")
    #img = Image.open(BytesIO(image_path.read()))
    #image = np.asarray(img)
    image = cv2.resize(image, dsize=input_shape, interpolation=cv2.INTER_CUBIC)
    # Scale values to [0, 1].
    image = image / 255.0
    # The model expects an input of (?, 224, 224, 3).
    images = np.expand_dims(image, 0)
    # This assumes you're using TF2.
    output = model(images)
    predicted_index = output.numpy().argmax()
    print("Prediction: ", model_label_map_classes[predicted_index])
    return model_label_map_classes[predicted_index]

def request_nutrition(food_item):
    response = requests.get(f'https://api.edamam.com/api/nutrition-data?app_id=8997459b&app_key={EDAMAME_KEY}&nutrition-type=logging&ingr={food_item}').json()
    if response is None:
        return None

    output = {
        "name" : food_item,
        "calories" : response['calories'],
        "protein": response['totalNutrients']['PROCNT']['quantity'],
        "carbohydrates": response['totalNutrients']['CHOCDF.net']['quantity'],
        "fat": response['totalNutrients']['FAT']['quantity'],
        "sugar": response['totalNutrients']['SUGAR']['quantity'],
        "carbon": response['totalCO2Emissions'],
        "carbon_class": response['co2EmissionsClass']
    }
    print(output)
    return output

def nutr_from_img(img_path):
    hi = predict_image(img_path)
    print('POST-MODEL: ', hi)
    return request_nutrition(hi)
    
# prediciton = predict_image(test_url)
# proper_json = request_nutrition(prediciton)
# print(proper_json)
    
