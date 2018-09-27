from keras_classifier.vgg16 import VGG16

from classifiers.common import *
from keras.datasets import mnist
import numpy as np
from keras import backend as K
import keras
import cv2
import os

def digits_load_data(path):
    classes = os.listdir(path)
    X = []
    y = []

    for clazz in classes:
        print(clazz)
        files = os.listdir(os.path.join(path, clazz))
        for file in files:
            img = os.path.join(path, clazz, file)
            # print(img)
            y.append(int(clazz))
            X.append(cv2.imread(img))


    print("len: ", len(X), " ", len(y))
    return (X, y)

def resizeAllImages(imgs, size):
    # print(imgs.shape)
    new_imgs = []
    for img in imgs:
        new_img = cv2.resize(img, size)
        new_imgs.append(new_img)

    return np.asarray(new_imgs)


batch_size = 16
num_classes = 2
epochs = 12

# input image dimensions
img_rows, img_cols = 80, 80

path_data = "/home/anderson/projetos/portaria_inteligente/placas"
# the data, split between train and test sets
(x_train, y_train) = digits_load_data(path_data)

x_train = resizeAllImages(x_train, (img_rows, img_cols))
print(type(x_train))
print(x_train.shape)
print(x_train.shape[3])

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], x_train.shape[3], img_rows, img_cols)
    input_shape = (x_train.shape[3], img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, x_train.shape[3])
    input_shape = (img_rows, img_cols, x_train.shape[3])

x_train = x_train.astype('float32')
x_train /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)

net = VGG16()

print("[+] BUILD")
model = net.build_network(input_shape, num_classes)

print("[+] COMPILE")
model = compile_net(model)

print("[+] TRAIN")
teste = train(model, x_train, y_train, None, None, batch_size, epochs, "binary_0_1", split=0.3)

print("[+] EVALUATE")
score = evaluate(teste, x_test, y_test)
