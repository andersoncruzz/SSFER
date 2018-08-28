from faceDetector.faceDetector import FaceDetector
from preProcessing.preProcessing import PreProcessing

faceDetector = FaceDetector()
preProcessing = PreProcessing()

#imgs = preProcessing.loadAllImagesWithSize(size=(60,60), save=True)
imgs = preProcessing.loadFromFile("databases/image_size_60_.npy")
print("len: ", len(imgs))

def expFaceDetector(imgs, faceDetector):
    #[TP, FN, FP, TN]
    matrix_confusion_ViolaJones = [0, 0, 0, 0]
    matrix_confusion_HogSvm = [0, 0, 0, 0]
    matrix_confusion_Cnn = [0, 0, 0, 0]
    for img in imgs:
        # detectionsVJ = faceDetector.detectViolaJones(img)
        # if len(detectionsVJ) > 0:
        #     matrix_confusion_ViolaJones[0] += 1
        # else:
        #     matrix_confusion_ViolaJones[1] += 1

        detectionsSVM = faceDetector.detectHogSVM(img)
        if len(detectionsSVM) > 0:
            matrix_confusion_HogSvm[0] += 1
        else:
            matrix_confusion_HogSvm[1] += 1


        detectionsCNN = faceDetector.detectCNN(img)
        if len(detectionsCNN) > 0:
            matrix_confusion_Cnn[0] += 1
        else:
            matrix_confusion_Cnn[1] += 1

    print("Viola Jones: ", matrix_confusion_ViolaJones)
    print("HOG SVM: ", matrix_confusion_HogSvm)
    print("CNN: ", matrix_confusion_Cnn)

expFaceDetector(imgs, faceDetector)
