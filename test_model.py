# -*coding: utf-8 -*-
import cv2
import sys
import numpy as np
import os
import sklearn.metrics as mt
from classifiers.common import Common
from preProcessing.preProcessing import PreProcessing
from keras import backend as K
import keras
# import tensorflow as tf

preProcessing = PreProcessing()

CLASSES = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']

PATH_DATABASE = "input_data_emotions"
INPUT_DATASET = "output_60"
PATH_DATABASE_INPUT = os.path.join(PATH_DATABASE, INPUT_DATASET)

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


#models/mybase_preload_0_9_300_ep_vgg16/weights.01-0.02.hdf5
PATH_MODELS = "models_experiment"

for PATH_WEIGHTS in os.listdir(PATH_MODELS):
    # PATH_WEIGHTS = "MobileNet+60+23_05_40+2018-11-01"
    for MODEL in os.listdir(os.path.join(PATH_MODELS, PATH_WEIGHTS)):
        if MODEL.find("hdf5") == -1:
            continue

        for BASE in ["validation", "testing", "training"]:
        # for BASE in ["validation"]:
            # MODEL = "weights.05-1.23.hdf5"
            PATH_WEIGHTS_INPUT = os.path.join(PATH_MODELS, PATH_WEIGHTS, MODEL)
            # PATH_WEIGHTS_INPUT = os.path.join(PATH_WEIGHTS, MODEL)

            REPORT_DIR = "reports"
            REPORT_FILE = os.path.join(REPORT_DIR, PATH_WEIGHTS, MODEL + "_"+BASE+".txt")


            #CREATING DIRECTORY
            make_dirs(os.path.join(REPORT_DIR, PATH_WEIGHTS))

            # the data, split between train and test sets
            # (x_test, y_true, CLASSES) = load_data(PATH_DATABASE_INPUT)
            X_train, y_true = preProcessing.load_base_for_validation(os.path.join(PATH_DATABASE_INPUT, BASE))

            common = Common()
            net = common.load_model_net(PATH_WEIGHTS_INPUT)

            file_report = open(REPORT_FILE, 'a')

            y_pred = []

            for img in X_train:
                img = np.array(img)
                # img = img.astype('float32')
                # img /= 255

                img = img.reshape(1, 60, 60, 3)

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
            K.clear_session()
