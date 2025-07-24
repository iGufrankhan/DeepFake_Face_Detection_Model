
# 🔄 train.py
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, BatchNormalization, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import LearningRateScheduler
import tensorflow as tf

dataset_path = "real_and_fake_face"

# Data augmentation
data_gen = ImageDataGenerator(rescale=1./255, horizontal_flip=True, validation_split=0.2)
train = data_gen.flow_from_directory(dataset_path, target_size=(96, 96), batch_size=32, class_mode="binary", subset="training")
val = data_gen.flow_from_directory(dataset_path, target_size=(96, 96), batch_size=32, class_mode="binary", subset="validation")

# Base Model
base_model = MobileNetV2(input_shape=(96, 96, 3), include_top=False, weights="imagenet")
base_model.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(512, activation="relu"),
    BatchNormalization(),
    Dropout(0.3),
    Dense(128, activation="relu"),
    Dropout(0.1),
    Dense(2, activation="softmax")
])

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.summary()

# Learning rate scheduler
def scheduler(epoch):
    if epoch <= 2:
        return 0.001
    elif epoch <= 15:
        return 0.0001
    return 0.00001

lr_callback = LearningRateScheduler(scheduler)

# Train the model
history = model.fit(train, epochs=20, validation_data=val, callbacks=[lr_callback])

# Save the model
model.save("deepfake_detection_model.h5")

# Plot accuracy and loss
plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label="Train Loss")
plt.plot(history.history['val_loss'], label="Val Loss")
plt.legend()
plt.title("Training vs Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.savefig("Figure_1.png")

plt.figure(figsize=(8, 5))
plt.plot(history.history['accuracy'], label="Train Acc")
plt.plot(history.history['val_accuracy'], label="Val Acc")
plt.legend()
plt.title("Training vs Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.savefig("Figure_2.png")