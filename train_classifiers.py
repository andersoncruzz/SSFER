from classifiers.vgg16 import VGG16
from classifiers.vgg19 import VGG19
from classifiers.resnet50 import ResNet50
from classifiers.mobilenet import MobileNet
from classifiers.mobilenetv2 import MobileNetV2
from classifiers.inceptionV3 import InceptionV3
from classifiers.inceptionResNetV2 import InceptionResNetV2

from classifiers.common import Common

import numpy as np
from keras import backend as K
import keras
import cv2
from preProcessing.preProcessing import PreProcessing
from utils.functions import make_dirs, get_date_string
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--img_size", required=True, type=int,
	help="img_size")
ap.add_argument("-lr", "--learning_rate", required=True, type=float,
	help="learning_rate")
ap.add_argument("-opt", "--optimizer", required=True, type=int,
	help="optmizer")
ap.add_argument("-arc", "--architecture", required=True, type=int,
	help="architecture")
ap.add_argument("-batch", "--batch_size", required=True, type=int,
	help="architecture")

args = vars(ap.parse_args())

preProcessing = PreProcessing()
common = Common()

# IMG_SIZE = 110
# LEARNING_RATE = 0.01
# BATCH_SIZE = 28
IMG_SIZE = args["img_size"]
LEARNING_RATE = args["learning_rate"]
BATCH_SIZE = args["batch_size"]


OPTIMIZERS = ["Adadelta", "SGD", "Nadam", "RMSprop"]
# OPTIMIZER = OPTIMIZERS[0]
OPTIMIZER = OPTIMIZERS[args["optimizer"]]

ARCHITECTURES = ["VGG16", "VGG19", "MobileNet", "MobileNetV2", \
                "ResNet50", "InceptionV3", "InceptionResNetV2"]
# ARCHITECTURE = ARCHITECTURES[3]
ARCHITECTURE = ARCHITECTURES[args["architecture"]]

ROOT_OUTPUT = "models_experiment"
EXPERIMENT_ID = ARCHITECTURE + "+" + str(IMG_SIZE) + "+" + get_date_string()
output_path = os.path.join(ROOT_OUTPUT, EXPERIMENT_ID)
make_dirs(output_path)

NUM_CLASSES = 7
EPOCHS = 1000

ROOT_INPUT_DATA = "input_data_emotions"
BASE_DIR = "output_"+str(IMG_SIZE)

common.write_file_info(output_path, ["architecture: " + ARCHITECTURE, "img_size: " + str(IMG_SIZE)])

input_path = os.path.join(ROOT_INPUT_DATA, BASE_DIR)
x_train, y_train, x_test, y_test = preProcessing.load_base_input_experiment(input_path)

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 3, IMG_SIZE, IMG_SIZE)
    input_shape = (3, IMG_SIZE, IMG_SIZE)
else:
    x_train = x_train.reshape(x_train.shape[0], IMG_SIZE, IMG_SIZE, 3)
    input_shape = (IMG_SIZE, IMG_SIZE, 3)

# x_train = x_train.astype('float32')
# x_train /= 255.0

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')

print("[+] TYPE NDARRAY: ", x_train.dtype)

# # convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)
y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)

print("[+] " + ARCHITECTURE)
if ARCHITECTURE == "VGG16":
    net = VGG16()
elif ARCHITECTURE == "VGG19":
    net = VGG19()
elif ARCHITECTURE == "MobileNet":
    net = MobileNet()
elif ARCHITECTURE == "MobileNetV2":
    net = MobileNetV2()
elif ARCHITECTURE == "ResNet50":
    net = ResNet50()
elif ARCHITECTURE == "InceptionV3":
    net = InceptionV3()
elif ARCHITECTURE == "InceptionResNetV2":
    net = InceptionResNetV2()

print("[+] BUILD")
model = net.build_network(input_shape, NUM_CLASSES)

print("[+] COMPILE")
model = common.compile_net(model, output_path, LEARNING_RATE, OPTIMIZER)

print("[+] TRAIN")
model, history = common.train(model, x_train, y_train, x_test, y_test, BATCH_SIZE, EPOCHS, output_path)

print("[+] SAVE ON HISTORY")
common.save_plot_losses(history, output_path)
common.save_plot_acc(history, output_path)
