# 🧠 DeepFake Face Detection Model using AI/ML

This project uses Convolutional Neural Networks (CNNs) and the MobileNetV2 architecture to detect manipulated facial images (deepfakes). It includes a Streamlit-based frontend for user-friendly interaction and a trained model to distinguish real and fake faces.

---

## 🚀 Features

- 📷 Upload any image and get real/fake classification
- 🧠 Trained on MobileNetV2 for fast and accurate prediction
- 📊 Live training accuracy/loss visualizations
- 🎯 Accuracy achieved: **95%**

---

## 🧪 Project Internship Details

This project was completed as part of the:

### **CYBER GYAN Virtual Internship Program**  
**Centre for Development of Advanced Computing (CDAC), Noida**  
🗓️ Duration: **June–July 2025**

**Submitted By:**  
- 👨‍💻 Name: **Gufran Khan**   

**Mentor:**  
- 👨‍🏫 **Varun Mishra**  
- 🧠 **Project Title:** Detect Manipulated Facial Images using AI/ML  

---

## 🖥️ Technologies Used

- Python 3.11+
- TensorFlow / Keras
- OpenCV
- Streamlit
- MobileNetV2
- Matplotlib

---

## 📁 Folder Structure

```bash
├── app.py                # Streamlit App
├── train.py              # Model training script
├── predict.py            # Image prediction logic
├── deepfake_detection_model.h5  # Trained model
├── Figure_1.png          # Loss graph
├── Figure_2.png          # Accuracy graph
├── cover.jpg             # App Cover Image
├── requirements.txt      # Required libraries
└── README.md             # This file

---


▶️ How to Run the App
Clone the repo:

bash
Copy
Edit
git clone https://github.com/iGufrankhan/DeepFake_Face_Detection_Model.git
cd DeepFake_Face_Detection_Model


(Optional) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
Install requirements:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py




