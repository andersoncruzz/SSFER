from keras_classifier.vgg16 import VGG16

from classifiers.common import *
from keras.datasets import mnist
import numpy as np
from keras import backend as K
import keras
import cv2


def resizeAllImages(imgs, size):
    new_imgs = []
    for img in imgs:
        if img.shape != ():
            new_img = cv2.resize(img, size)
            new_imgs.append(new_img)

    return np.asarray(new_imgs)


batch_size = 16
num_classes = 10
epochs = 12

# input image dimensions
img_rows, img_cols = 90, 90

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = resizeAllImages(x_train, (img_rows, img_cols))
x_test = resizeAllImages(x_test, (img_rows, img_cols))

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print("[+] VGG")
net = VGG16()

print("[+] BUILD")
model = net.build_network(input_shape, num_classes)

# print("[+] LAST LAYER")
# model =  add_last_layer(net, num_classes)

print("[+] COMPILE")
model = compile_net(model)

print("[+] TRAIN")
teste = train(model, x_train, y_train, x_test, y_test, batch_size, epochs, "mnist")

print("[+] EVALUATE")
score = evaluate(teste, x_test, y_test)
