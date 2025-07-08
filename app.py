import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array


st.markdown("""
    <style>
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #262730;
            color: white;
            text-align: center;
            padding: 20px;
            font-size: 28px;
            font-weight: bold;
            z-index: 9999;
        }
        .space-below {
            margin-top: 90px; 
        }
        .stButton > button {
            font-size: 16px;
            padding: 0.75em 1.5em;
            border-radius: 8px;
        }
    </style>
    <div class="fixed-header">
       🤖 DEEPFAKE FACE DETECTION MODEL
    </div>
    <div class="space-below"></div>
""", unsafe_allow_html=True)

st.image("cover.jpg", use_container_width=True)

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

st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🧠 Upload Image for Deepfake Detection")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR", use_container_width=True)
    result = predict_image(image)
    color = "red" if result == "Fake" else "green"
    st.markdown(f"<h2 style='color:{color}; text-align:center;'>The image is {result}</h2>", unsafe_allow_html=True)

st.title("📈 Model Training Results")
st.markdown("### Model Accuracy: 95%")
st.image("Figure_2.png", use_container_width=True)
st.markdown("### Model Loss Curve")
st.image("Figure_1.png", use_container_width=True)

st.markdown("""---  
**Contact Us:** [contact@example.com](mailto:contact@example.com)  
**Follow us:** [Twitter](https://twitter.com) | [LinkedIn](https://linkedin.com) | [Facebook](https://facebook.com)  
""")
