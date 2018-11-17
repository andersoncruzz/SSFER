# -*- coding: utf-8 -*-

import argparse
import sys
import time

import cv2
from keras import backend as K
import keras
from keras.models import load_model
import sys, os
from faceDetector.faceDetector import FaceDetector
import numpy as np

def padding_bounding_box(bb, img_size, padding=32):
    bounding_box = np.zeros(4, dtype=np.int32)

    bounding_box[0] = np.maximum(bb[3] - padding / 2, 0)
    bounding_box[1] = np.maximum(bb[0] - padding / 2, 0)
    bounding_box[2] = np.minimum(bb[1] + padding / 2, img_size[1])
    bounding_box[3] = np.minimum(bb[2] + padding / 2, img_size[0])

    return bounding_box


def get_emotion(net, img, coordinate):

    img_cropped = img[coordinate[0]:coordinate[2], coordinate[3]:coordinate[1]]
    # cv2.imshow("cropped", img_cropped)
    # cv2.waitKey(1)

    # img_cropped = cv2.resize(img_cropped, (80, 80))
    # img_cropped = np.array(img_cropped)
    # img_cropped = img_cropped.reshape(1, 80, 80, 3)
    # predictions = net.predict([np.array(img_cropped)])
    # index_emotion = np.argmax(predictions[0])

    return 6

def classify(net, img, faceDetector):
    faces = []
    img_size = np.asarray(img.shape)[0:2]
    coordinates = faceDetector.detectHogSVM(img)

    for coordinate in coordinates:
        face = {}
        face["bounding_box"] = padding_bounding_box(coordinate, img_size)
        face["emotion"] = get_emotion(net, img, coordinate)
        faces.append(face)

    return faces

def add_overlays(frame, faces, frame_rate, EMOTIONS, feelings_faces):
    if faces is not None:
        for face in faces:
            face_bb = face["bounding_box"]
            cv2.rectangle(frame,
                          (face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]),
                          (0, 255, 0), 2)
            if face["emotion"] is not None:
                # print("Person: ", face.name)
                cv2.putText(frame, EMOTIONS[face["emotion"]], (face_bb[0], face_bb[3]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                            thickness=2, lineType=2)

                emoji = feelings_faces[face["emotion"]]
                # Ugly transparent fix
                for c in range(0, 3):
                    frame[face_bb[1]:face_bb[1]+120, face_bb[0]:face_bb[0]+120, c] = emoji[:,:,c] * (emoji[:, :, 3] // 255.0) +  frame[face_bb[1]:face_bb[1]+120, face_bb[0]:face_bb[0]+120, c] * (1.0 - emoji[:, :, 3] // 255.0)



    cv2.putText(frame, str(frame_rate) + " fps", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                thickness=2, lineType=2)


def main(args):

    EMOTIONS = ['angry', 'disgusted', 'fearful', \
            'happy', 'sad', 'surprised', 'neutral']

    EMOTIONS_pt = ['raiva', 'desgosto', 'medo', \
            'felicidade', 'tristeza', 'surpresa', 'neutralidade']


    feelings_faces = []
    for index, emotion in enumerate(EMOTIONS):
        feelings_faces.append(cv2.imread('./emojis/' + emotion + '.png', -1))


    PATH_NET_INPUT = ""

    frame_interval = 5  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0
    capture = 0
    print("capture: ", capture)
    video_capture = cv2.VideoCapture(capture)
    print("[+] LOADING: ")

    # net = load_model(PATH_NET_INPUT)
    net = None

    faceDetector = FaceDetector()
    start_time = time.time()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("QUIT APPLICATION")
            break

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if (frame_count % frame_interval) == 0:
            # faces = face_recognition.classify(frame)
            faces = classify(net, frame, faceDetector)

            # Check our current fps
            end_time = time.time()
            if (end_time - start_time) > fps_display_interval:
                frame_rate = int(frame_count / (end_time - start_time))
                start_time = time.time()
                frame_count = 0

        add_overlays(frame, faces, frame_rate, EMOTIONS_pt, feelings_faces)

        frame_count += 1
        cv2.imshow('Video', frame)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

def parse_arguments(argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action='store_true',
                        help='Enable some debug outputs.')
    return parser.parse_args(argv)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
