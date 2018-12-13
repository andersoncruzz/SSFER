import os
import numpy as np
import pandas as pd
import cv2

labels_PATH = 'databases/VOC2007/ImageSets/Main/person_test.txt'
images_PATH = 'databases/VOC2007/JPEGImages'

data = pd.read_csv(labels_PATH, delim_whitespace=True, dtype={"Image": str})

images = []
labels = []

for index, row in data.iterrows():
    image_path = os.path.join(images_PATH, row["Image"]+".jpg")
    img = cv2.imread(image_path)
    print(img.shape)
    images.append(img)
    label = row["label"]
    labels.append(label)

np.save("databases/VOC2007-data.npy", images)
np.save("databases/VOC2007-labels.npy", labels)

