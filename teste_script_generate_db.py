from preProcessing.preProcessing import PreProcessing
from faceDetector.faceDetector import FaceDetector

preProcessing = PreProcessing()
faceDetector = FaceDetector()

size = 60
path_output = "output_"+str(size)
preProcessing.save_images_labels_size(size, faceDetector, path_output)
