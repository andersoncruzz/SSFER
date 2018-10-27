from faceDetector.faceDetector import FaceDetector
from preProcessing.preProcessing import PreProcessing

faceDetector = FaceDetector()
preProcessing = PreProcessing()

#imgs = preProcessing.loadAllImagesWithSize(size=(60,60), save=True)
# imgs = preProcessing.loadFromFile("databases/image_size_60_.npy")

def expFaceDetector(preProcessing, faceDetector):
    #[TP, FN, FP, TN]
    imgs = preProcessing.loadFromFile("databases/image_size_60_.npy")
    total = len(imgs)
    index = 1
    matrix_confusion_ViolaJones = [0, 0, 0, 0]
    matrix_confusion_HogSvm = [0, 0, 0, 0]
    matrix_confusion_Cnn = [0, 0, 0, 0]
    for img in imgs:
        detectionsVJ = faceDetector.detectViolaJones(img)
        if len(detectionsVJ) > 0:
            matrix_confusion_ViolaJones[0] += 1
        else:
            matrix_confusion_ViolaJones[1] += 1

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

        index += 1
        print ("{}/{} {:.2f}%".format(index, total, index * 100.0 / total))

        print("Viola Jones: ", matrix_confusion_ViolaJones)
        print("HOG SVM: ", matrix_confusion_HogSvm)
        print("CNN: ", matrix_confusion_Cnn)

def expNoFaceDetector(preProcessing, faceDetector):
    imgs = preProcessing.loadFromFile("databases/VOC2007-data.npy")
    labels = preProcessing.loadFromFile("databases/VOC2007-labels.npy")
    total = len(imgs)
    index = 0
    #["0, 0, 0, 0"]
    #Acerto (Sem Pessoa, Sem Face); Acerto (Com Pessoa, Com Face); Acerto (Com Pessoa, Sem Face)
    #Erro (Sem Pessoa, Com Face)
    matrix_confusion_ViolaJones = [0, 0, 0, 0]
    matrix_confusion_HogSvm = [0, 0, 0, 0]
    matrix_confusion_Cnn = [0, 0, 0, 0]

    #DATABASE FER
    # Viola Jones:  [21855, 73459, 0, 0]
    # HOG SVM:  [54790, 40524, 0, 0]
    # CNN:  [79966, 15348, 0, 0]

    #VOC2007
    # 4952/4952 100.00%
    # Viola Jones:  [507, 2905, 1500, 40]
    # HOG SVM:  [711, 2915, 1296, 30]
    # CNN:  [829, 2932, 1178, 13]


    for index in range(total):
        detectionsVJ = faceDetector.detectViolaJones(imgs[index])

        #Acerto Com Face Com Pessoa
        if len(detectionsVJ) > 0 and labels[index] == 1:
            matrix_confusion_ViolaJones[0] += 1
        #Acerto Sem Face Sem Pessoa
        elif (len(detectionsVJ) == 0 and labels[index] == -1) or (len(detectionsVJ) == 0 and labels[index] == 0):
            matrix_confusion_ViolaJones[1] += 1
        #Acerto Sem Face Com Pessoa
        elif len(detectionsVJ) == 0 and labels[index] == 1:
            matrix_confusion_ViolaJones[2] += 1
        #Erro Com Face Sem Pessoa
        elif (len(detectionsVJ) > 0 and labels[index] == -1) or (len(detectionsVJ) > 0 and labels[index] == 0):
            matrix_confusion_ViolaJones[3] += 1

        else:
            print("AQUI PORRA")
            print("Detct: ", len(detectionsVJ), "label: ", labels[index])
            break

        detectionsSVM = faceDetector.detectHogSVM(imgs[index])
        #Acerto Com Face Com Pessoa
        if len(detectionsSVM) > 0 and labels[index] == 1:
            matrix_confusion_HogSvm[0] += 1
        #Acerto Sem Face Sem Pessoa
        elif (len(detectionsSVM) == 0 and labels[index] == -1) or (len(detectionsSVM) == 0 and labels[index] == 0):
            matrix_confusion_HogSvm[1] += 1
        #Acerto Sem Face Com Pessoa
        elif len(detectionsSVM) == 0 and labels[index] == 1:
            matrix_confusion_HogSvm[2] += 1
        #Erro Com Face Sem Pessoa
        elif (len(detectionsSVM) > 0 and labels[index] == -1) or (len(detectionsSVM) > 0 and labels[index] == 0):
            matrix_confusion_HogSvm[3] += 1


        detectionsCNN = faceDetector.detectCNN(imgs[index])
        #Acerto Com Face Com Pessoa
        if len(detectionsCNN) > 0 and labels[index] == 1:
            matrix_confusion_Cnn[0] += 1
        #Acerto Sem Face Sem Pessoa
        elif (len(detectionsCNN) == 0 and labels[index] == -1) or (len(detectionsCNN) == 0 and labels[index] == 0):
            matrix_confusion_Cnn[1] += 1
        #Acerto Sem Face Com Pessoa
        elif len(detectionsCNN) == 0 and labels[index] == 1:
            matrix_confusion_Cnn[2] += 1
        #Erro Com Face Sem Pessoa
        elif (len(detectionsCNN) > 0 and labels[index] == -1) or (len(detectionsCNN) > 0 and labels[index] == 0):
            matrix_confusion_Cnn[3] += 1

        index += 1
        print ("{}/{} {:.2f}%".format(index, total, index * 100.0 / total))

        print("Viola Jones: ", matrix_confusion_ViolaJones)
        print("HOG SVM: ", matrix_confusion_HogSvm)
        print("CNN: ", matrix_confusion_Cnn)


# expFaceDetector(preProcessing, faceDetector)
expNoFaceDetector(preProcessing, faceDetector)
