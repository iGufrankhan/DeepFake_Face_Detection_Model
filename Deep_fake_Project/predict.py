
# 🔄 predict.py
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load trained model once
model = load_model('deepfake_detection_model.h5')

def preprocess_image(image):
    image = cv2.resize(image, (96, 96))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image

def predict_image(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    class_label = np.argmax(prediction, axis=1)[0]
    return "Fake" if class_label == 0 else "Real"
