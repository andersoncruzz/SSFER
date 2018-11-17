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

def padding_bounding_box(bbs, img_size, padding=32):
    bounding_boxxes = []
    for bb in bbs:
        bounding_box = np.zeros(4, dtype=np.int32)

        bounding_box[0] = np.maximum(bb[3] - padding / 2, 0)
        bounding_box[1] = np.maximum(bb[0] - padding / 2, 0)
        bounding_box[2] = np.minimum(bb[1] + padding / 2, img_size[1])
        bounding_box[3] = np.minimum(bb[2] + padding / 2, img_size[0])
        bounding_boxxes.append(bounding_box)

    return bounding_boxxes


def classify(net, img, faceDetector):
    faces = []
    # img = cv2.resize(img, (80, 80))
    # img = np.array(img)
    # img = img.reshape(1, 80, 80, 3)
    # predictions = net.predict([np.array(img)])
    # index_emotion = np.argmax(predictions[0])
    img_size = np.asarray(img.shape)[0:2]
    coordinates = faceDetector.detectHogSVM(img)
    coordinates = padding_bounding_box(coordinates, img_size)

    for coordinate in coordinates:
        face = {}
        face["bounding_box"] = coordinate
        face["emotion"] = "Neutralidade"
        faces.append(face)

    return faces

def add_overlays(frame, faces, frame_rate):
    if faces is not None:
        for face in faces:
            face_bb = face["bounding_box"]
            cv2.rectangle(frame,
                          (face_bb[0], face_bb[1]), (face_bb[2], face_bb[3]),
                          (0, 255, 0), 2)
            if face["emotion"] is not None:
                # print("Person: ", face.name)
                cv2.putText(frame, face["emotion"], (face_bb[0], face_bb[3]),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                            thickness=2, lineType=2)

    cv2.putText(frame, str(frame_rate) + " fps", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                thickness=2, lineType=2)


def main(args):
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

        add_overlays(frame, faces, frame_rate)

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
