# 🔍 Deepfake Detection System using MobileNetV2 & Streamlit

> A powerful AI-based system to detect manipulated or synthetic (deepfake) images and videos using lightweight deep learning models. Developed as part of the **Cyber Gyan Virtual Internship Program**, CDAC Noida – July 2025.

![Streamlit UI Screenshot](app.png)

---

## 📅 Project Timeline
- **Start Date:** July 1, 2025  
- **Completion Date:** July 8, 2025  
- **Mentor:** Mr. Varun Mishra  
- **Organized By:** CDAC Noida - Cyber Gyan Virtual Internship Program

---

## 🧠 Problem Statement

Cybercriminals increasingly use deep learning technologies to manipulate facial media content for malicious purposes—ranging from fake news to financial fraud and explicit deepfakes. This project aims to **design and develop an intelligent detection system** to identify such tampered or fake media.

---

## 🛠️ Tools & Technologies

| Component              | Technology Used               |
|------------------------|-------------------------------|
| Model Architecture     | MobileNetV2 (TensorFlow/Keras)|
| Frontend               | Streamlit                     |
| Image Processing       | OpenCV                        |
| Dataset Augmentation   | ImageDataGenerator            |
| Deployment             | Streamlit Cloud / Localhost   |
| Programming Language   | Python 3.10                   |

---

## 🧪 Features

- Upload image and detect if it's **REAL** or **DEEPFAKE**
- Built using **pre-trained MobileNetV2**
- Streamlit-based **interactive web interface**
- Realtime model prediction & clean UI
- Lightweight and optimized for fast inference

---

## 🚀 Project Structure

```bash
.
├── app.py                # Streamlit UI
├── predict.py            # Prediction logic
├── train.py              # Model training script
├── deepfake_model.h5     # Trained Keras model
├── dataset/              # Images (real and fake)
├── screenshots/          # Screenshots of the app
└── requirements.txt


🖥️ How to Run Locally
git clone https://github.com/yourusername/deepfake-detection
cd deepfake-detection
pip install -r requirements.txt
streamlit run app.py
🔗 Dataset Used
We used the following dataset to train and test our deepfake detection model:

📁 Real and Fake Face Detection Dataset – Kaggle

Contains high-resolution real and fake face images.

Generated using advanced GAN architectures.

Suitable for face manipulation detection tasks.

🙏 Thank You
This project was completed under the guidance of Mr. Varun Mishra as part of the Cyber Gyan Virtual Internship Program organized by CDAC Noida







