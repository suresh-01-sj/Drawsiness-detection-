import os
import cv2
import numpy as np
from tqdm import tqdm

data_dir = "mrlEyes_2018_01"
images = []
labels = []

for folder in os.listdir(data_dir):
    folder_path = os.path.join(data_dir, folder)
    if os.path.isdir(folder_path):
        for file in tqdm(os.listdir(folder_path), desc=folder):
            if file.endswith(".png"):
                label = int(file.split("_")[4])  # 0=open, 1=closed
                img_path = os.path.join(folder_path, file)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img, (80, 80))
                images.append(img)
                labels.append(label)

X = np.array(images).reshape(-1, 80, 80, 1) / 255.0
y = np.array(labels)

np.save("X.npy", X)
np.save("y.npy", y)
print(f"Saved {len(X)} images.")
