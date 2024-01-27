# TF2 version
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd
import cv2
from skimage import io
import os

root_dir = os.path.dirname(__file__)
labelmap_dir = os.path.join(root_dir, "model/aiy_food_V1_labelmap.csv")
model_dir = os.path.join(root_dir, "model/")
# images_dir = os.path.

# model = hub.KerasLayer('https://www.kaggle.com/models/google/aiy/frameworks/TensorFlow1/variations/vision-classifier-food-v1/versions/1')
model = hub.KerasLayer(model_dir)

test_url = "https://www.allrecipes.com/thmb/5JVfA7MxfTUPfRerQMdF-nGKsLY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/25473-the-perfect-basic-burger-DDMFS-4x3-56eaba3833fd4a26a82755bcd0be0c54.jpg"
input_shape = (224, 224)

# Food classification model from https://www.kaggle.com/models/google/aiy/frameworks/tensorFlow1/variations/vision-classifier-food-v1

def PredictImage(image_path):
    image = np.asarray(io.imread(image_path), dtype="float")
    image = cv2.resize(image, dsize=input_shape, interpolation=cv2.INTER_CUBIC)
    # Scale values to [0, 1].
    image = image / image.max()
    # The model expects an input of (?, 224, 224, 3).
    images = np.expand_dims(image, 0)
    # This assumes you're using TF2.
    output = model(images)
    predicted_index = output.numpy().argmax()
    classes = list(pd.read_csv(labelmap_dir)["name"])
    print("Prediction: ", classes[predicted_index])

PredictImage(test_url)
    
# def get_nutrition(food):
    
