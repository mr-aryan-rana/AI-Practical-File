import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import random
data_dir = r"D:\AI\archive\brain_tumor_dataset"
img_size = (128, 128)
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train = datagen.flow_from_directory(data_dir, target_size=img_size, subset='training', class_mode='binary')
val = datagen.flow_from_directory(data_dir, target_size=img_size, subset='validation', class_mode='binary')
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=img_size+(3,)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(train, validation_data=val, epochs=5)
sample_images = random.sample(val.filepaths, 3)
plt.figure(figsize=(12, 4))  # wide figure for single-row display
for i, path in enumerate(sample_images):
    img = cv2.imread(path)
    img_resized = cv2.resize(img, img_size)
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    marked = img_resized.copy()
    cv2.drawContours(marked, contours, -1, (255, 0, 0), 2)
    plt.subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(marked, cv2.COLOR_BGR2RGB))
    plt.title(f"Tumor: {'Yes' if 'yes' in path else 'No'}", fontsize=8)
    plt.suptitle("Name : Aryan Rana | Roll No. : 1323223", fontsize=10)
    plt.axis('off')
plt.tight_layout()
plt.show()
