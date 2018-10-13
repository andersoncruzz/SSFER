from keras_classifier.vgg16 import VGG16

from classifiers.common import *
from keras.datasets import mnist
import numpy as np
from keras import backend as K
import keras
import cv2
from preProcessing.preProcessing import PreProcessing

preProcessing = PreProcessing()

batch_size = 16
num_classes = 7
epochs = 1000

# input image dimensions
img_rows, img_cols = 60, 60

base_dir = "output_60"
x_train, y_train = preProcessing.load_base(base_dir)

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 3, img_rows, img_cols)
    input_shape = (3, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 3)
    input_shape = (img_rows, img_cols, 3)

x_train = x_train.astype('float32')

x_train /= 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')

# # convert class vectors to binary class matrices
# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

print("[+] VGG")
net = VGG16()

print("[+] BUILD")
model = net.build_network(input_shape, num_classes)

print("[+] COMPILE")
model = compile_net(model)

print("[+] TRAIN")
teste = train(model, x_train, y_train, None, None, batch_size, epochs, "emotion_vgg")

# print("[+] EVALUATE")
# score = evaluate(teste, x_test, y_test)
