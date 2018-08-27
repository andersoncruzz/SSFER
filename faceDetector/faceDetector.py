import face_recognition
import cv2
import numpy as np

class FaceDetector:
    # def __init__(self):
    #     pass

    def detectViolaJones(self, img, SF = 1.01, casc_path):
        #TODO: Verify params ViolaJones, IS REALLY VIOLA JONES ALGORITHM?
        cascade_classifier = cv2.CascadeClassifier(casc_path)
        faces = cascade_classifier.detectMultiScale(
            image,
            scaleFactor = SF,
            minNeighbors = 5
        )
        # None is we don't found an image
        if not len(faces) > 0:
            #print ("No hay caras")
            return None

        max_area_face = faces[0]
        for face in faces:
            if face[2] * face[3] > max_area_face[2] * max_area_face[3]:
                max_area_face = face
            # Chop image to face
            face = max_area_face
            print(face)
            #image = image[face[1]:(face[1] + face[2]), face[0]:(face[0] + face[3])]


    def detectHogSVM(self, img):
        return face_recognition.face_locations(img)

    def detectCNN(self, img, upsample=1):
        if img.size == 0:
            print("[+++] Entrou no None")
            return []

        return face_recognition.face_locations(img, number_of_times_to_upsample=upsample, model="cnn")
