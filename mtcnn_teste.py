from mtcnn.mtcnn import MTCNN
import cv2

image = cv2.imread("/home/anderson/Pictures/anderson.jpg")
# image = cv2.imread("/home/anderson/Desktop/2f571457-6c5d-413a-82c2-f232e1fe52d9-original.png")
detector = MTCNN()
result = detector.detect_faces(image)

# bounding_box = result[0]['box']
# keypoints = result[0]['keypoints']
#
# cv2.rectangle(image,
# (bounding_box[0], bounding_box[1]),
# (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
# (0,155,255),
# 2)
#
# cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
# cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
# cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
# cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
# cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)
#
# cv2.imshow("teste", image)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
#


# from faceDetector.faceDetector import FaceDetector
# import cv2
#
# image = cv2.imread("/home/anderson/Pictures/anderson.jpg")
# detector = FaceDetector(mtcnn=True)
# bounding_box = detector.detectMTCNN(image)
#
# cv2.rectangle(image,
#               (bounding_box[0], bounding_box[1]),
#               (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
#               (0,155,255),
#               2)
#
# cv2.imshow("teste", image)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
