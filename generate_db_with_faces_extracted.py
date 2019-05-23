from preProcessing.preProcessing import PreProcessing
from faceDetector.faceDetector import FaceDetector
import os

preProcessing = PreProcessing()
faceDetector = FaceDetector(mtcnn=True)

#60. 110, 160, 185, 210
size = 185
root = "emotions_database_with_faces_extracted"
path_output = os.path.join(root, "output_"+str(size))

preProcessing.save_images_labels_size(size, faceDetector, path_output)
