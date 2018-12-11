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

    img_cropped = cv2.resize(img_cropped, (110, 110))
    img_cropped = np.array(img_cropped)
    img_cropped = img_cropped.reshape(1, 110, 110, 3)
    predictions = net.predict([np.array(img_cropped)])
    index_emotion = np.argmax(predictions[0])

    return index_emotion

def ajust_point_on_view(point, img_size):
    if point + 120 > img_size:
        return point - (point + 120 - img_size)

    return point

def get_coordinate_emoji(bb, img_size):
    bounding_box = np.zeros(4, dtype=np.int32)

    bounding_box[0] = ajust_point_on_view(bb[0], img_size[1])
    bounding_box[1] = ajust_point_on_view(bb[1], img_size[0])
    bounding_box[2] = bb[0] + 120
    bounding_box[3] = bb[1] + 120

    return bounding_box

def classify(net, img, faceDetector, img_size):
    faces = []

    coordinates = faceDetector.detectMTCNN(img)
    # coordinates = faceDetector.detectHogSVM(img)
    print("BB: ", coordinates)
    for coordinate in coordinates:
        face = {}
        face["bounding_box"] = padding_bounding_box(coordinate, img_size)
        face["emotion"] = get_emotion(net, img, coordinate)
        faces.append(face)

    return faces

def add_overlays(frame, faces, frame_rate, EMOTIONS, feelings_faces, img_size):
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
                emoji_bb = get_coordinate_emoji(face_bb, img_size)
                # Ugly transparent fix
                for c in range(0, 3):
                    frame[emoji_bb[1]:emoji_bb[3], emoji_bb[0]:emoji_bb[2], c] = emoji[:,:,c] * (emoji[:, :, 3] // 255.0) +  frame[emoji_bb[1]:emoji_bb[3], emoji_bb[0]:emoji_bb[2], c] * (1.0 - emoji[:, :, 3] // 255.0)



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


    PATH_NET_INPUT = "model/vgg_19_weights_110+03_18_51+2018-11-1.hdf5"

    frame_interval = 5  # Number of frames after which to run face detection
    fps_display_interval = 5  # seconds
    frame_rate = 0
    frame_count = 0

    ROOT_VIDEO_PATH = os.path.expanduser("~/videos_intelbras")
    video = "20000101_011841.mp4"
    capture = os.path.join(ROOT_VIDEO_PATH, video)
    print("capture: ", capture)
    video_capture = cv2.VideoCapture(capture)
    print("[+] LOADING: ")

    net = load_model(PATH_NET_INPUT)

    faceDetector = FaceDetector(mtcnn=True)
    start_time = time.time()

    while (video_capture.isOpened()):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("QUIT APPLICATION")
            break

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if frame is None:
            break

        img_size = np.asarray(frame.shape)[0:2]

        if (frame_count % frame_interval) == 0:
            faces = classify(net, frame, faceDetector, img_size)

            # Check our current fps
            end_time = time.time()
            if (end_time - start_time) > fps_display_interval:
                frame_rate = int(frame_count / (end_time - start_time))
                start_time = time.time()
                frame_count = 0

        add_overlays(frame, faces, frame_rate, EMOTIONS_pt, feelings_faces, img_size)

        frame_count += 1
        # cv2.imshow('Video', frame)
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_GUI_EXPANDED)
        cv2.imshow("window", frame)

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
