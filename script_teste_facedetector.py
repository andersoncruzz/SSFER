import numpy as np
import os
from faceDetector.faceDetector import FaceDetector
import cv2

faceDetector = FaceDetector(mtcnn=True)
# faceDetector = FaceDetector()

matrix_confusion_ViolaJones = [0, 0, 0, 0]
matrix_confusion_HogSvm = [0, 0, 0, 0]
matrix_confusion_Cnn = [0, 0, 0, 0]
matrix_confusion_MTCnn = [0, 0, 0, 0]

pwd = "database"

DATA = ['RafD-data.npy', 'CIFE-data-ts.npy', 'ck+-data.npy', 'fer_data.npy', \
        'KDEF-data.npy', 'CIFE-data-tr.npy', 'novaemotions-data.npy', 'JAFFE-data.npy']
v_sum = 0

total = 95314
index = 1

for base in DATA:
    data_loaded = np.load(os.path.join(pwd, base))
    v_sum += data_loaded.shape[0]
    print(base)
    print(data_loaded.shape)

    for img in data_loaded:
        img = cv2.resize(img, (110, 110))

        detectionsMTCNN = faceDetector.detectMTCNN(img)

        if len(detectionsMTCNN) > 0:
            matrix_confusion_MTCnn[0] += 1
        else:
            matrix_confusion_MTCnn[1] += 1


        # detectionsVJ = faceDetector.detectViolaJones(img)
        # if len(detectionsVJ) > 0:
        #     matrix_confusion_ViolaJones[0] += 1
        # else:
        #     matrix_confusion_ViolaJones[1] += 1

        # detectionsSVM = faceDetector.detectHogSVM(img)
        # if len(detectionsSVM) > 0:
        #     matrix_confusion_HogSvm[0] += 1
        # else:
        #     matrix_confusion_HogSvm[1] += 1
        #
        #
        # detectionsCNN = faceDetector.detectCNN(img)
        # if len(detectionsCNN) > 0:
        #     matrix_confusion_Cnn[0] += 1
        # else:
        #     matrix_confusion_Cnn[1] += 1

        index += 1
        print ("{}/{} {:.2f}%".format(index, total, index * 100.0 / total))

    print("Viola Jones: ", matrix_confusion_ViolaJones)
    print("HOG SVM: ", matrix_confusion_HogSvm)
    print("CNN: ", matrix_confusion_Cnn)
    print("MTCNN: ", matrix_confusion_MTCnn)
    print("-----------------------------------")

    del data_loaded

print(v_sum)
