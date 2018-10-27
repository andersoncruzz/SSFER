# -*coding: utf-8 -*-
import cv2
import sys
import numpy as np
import os
import sklearn.metrics as mt
from classifiers.common import Common
from keras import backend as K
import keras

PATH_DATABASE = "database"
INPUT_DATASET = "digits_0_9"
PATH_DATABASE_INPUT = os.path.join(PATH_DATABASE, INPUT_DATASET)

#models/mybase_preload_0_9_300_ep_vgg16/weights.01-0.02.hdf5
PATH_MODELS = "models"
PATH_WEIGHTS = "digits_0_9_preload_300_ep_vgg16"
MODEL = "weights.05-0.00.hdf5"
PATH_WEIGHTS_INPUT = os.path.join(PATH_MODELS, PATH_WEIGHTS, MODEL)
# PATH_WEIGHTS_INPUT = os.path.join(PATH_WEIGHTS, MODEL)

REPORT_DIR = "reports"
REPORT_FILE = os.path.join(REPORT_DIR, PATH_WEIGHTS, MODEL + "_val.txt")

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
    return (X, y, classes)

def head(line):
    str_line = "\t"
    for item in line:
        str_line += str(item) + "\t"

    return str_line + "\n"

def line(line, clazz):
    str_line = str(clazz) + "\t"
    for item in line:
        str_line += str(item) + "\t"

    return str_line + "\n"

def confusion_matrix(y_true, y_pred, classes):
    rt = mt.confusion_matrix(y_true, y_pred)

    txt = head(classes)

    for i in enumerate(rt):
        txt += line(i[1], i[0])
    return txt

def make_dirs(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

#CREATING DIRECTORY
make_dirs(os.path.join(REPORT_DIR, PATH_WEIGHTS))

# the data, split between train and test sets
(x_test, y_true, CLASSES) = digits_load_data(PATH_DATABASE_INPUT)

common = Common()
net = common.load_model_net(PATH_WEIGHTS_INPUT)

file_report = open(REPORT_FILE, 'a')

y_pred = []

for img in x_test:
    img = np.array(img)
    img = img.astype('float32')
    img /= 255

    img = img.reshape(1, 80, 80, 3)

    result = net.predict([img])
    clazz_predicted = np.argmax(result)

    print("result:", result)
    print("clazz: ", clazz_predicted)

    y_pred.append(clazz_predicted)
    # y_true.append(np.argmax(labels[i]))

conf_matrix = confusion_matrix(y_true, y_pred, CLASSES)
acc_score = mt.accuracy_score(y_true, y_pred)
class_report = mt.classification_report(y_true, y_pred, target_names=CLASSES)
f1_score = mt.f1_score(y_true, y_pred, average=None)
precision_score = mt.precision_score(y_true, y_pred, average=None)
recall_score = mt.recall_score(y_true, y_pred, average=None)

print("Y_TRUE_LEN: ", len(y_true))
print("Y_PRED_LEN: ", len(y_pred))
print("----confusion_matrix----")
print(conf_matrix)
print("----accuracy_score----")
print(acc_score)
print("----classification_report----")
print(class_report)
print("----f1_score----")
print(f1_score)
print("----precision_score-------")
print(precision_score)
print("----recall_score-------")
print(recall_score)


txt = ""
txt += "Acuracia do modelo: " + MODEL + "\n"
txt += str(acc_score)

txt += "\n\nConfusion_matrix:\n"
txt += "\n" + str(conf_matrix)

txt += "\n\nClassification Report:\n"
txt += "\n" + str(class_report)
txt += "\n\n\n"

file_report.write(txt)
file_report.close()
