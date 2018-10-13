import cv2
import numpy as np
from utils.constants import getDataPath
from utils.constants import getDataAndLabelsPath
from utils.constants import getLabelsPath
import os

class PreProcessing:

    def generate_images_with_size(self, size, save=True, paths=None, path_output=None, faceDetector=None):
        # CIFE_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA = getDataPath()
        if paths == None:
            paths_images = getDataPath()
            path_labels = getLabelsPath()

        total_images = 0

        if len(paths_images) != len(path_labels):
            print("[+] ERROR PATH LABEL AND IMAGE SIZE DIFFERENCE")
            return False

        for index in range(len(paths_images)):
            print("path: ", paths_images[index])
            total_images += self.resize_all_images_label(size, paths_images[index], path_output, path_labels[index], faceDetector, save)

        print("[+] Total Images: ", total_images)
        return True

    # def generate_labels(self, save=False, paths=None, path_output=None):
    #     if paths == None:
    #         paths = getLabelsPath()
    #
    #     labels = []
    #
    #     # for path in enumerate(paths):
    #     for path in paths:
    #         label = np.load(path).tolist()
    #         labels += label
    #
    #     print("[+] Labels len: ", len(labels))
    #
    #     if save == True:
    #         self.make_dirs(os.path.join(path_output, "labels"))
    #         file_name = os.path.join(path_output, "labels",  "labels.npy")
    #         print("[+] File Saving: ", file_name)
    #         np.save(file_name, labels)
    #
    #
    #     return labels

    def load_from_file(self, path):
        return np.load(path)

    def resize_all_images_label(self, size, path_load, path_output, path_label, faceDetector=None, save=True):
        #TODO: Verify others possible resize processing, cubic, linear, etc, upsample
        new_images = []
        new_labels = []

        images = np.load(path_load)
        labels = np.load(path_label)

        print("[+] SIZE: ", size)

        if len(images) != len(labels):
            print("[+] ERROR LABEL AND IMAGE SIZE DIFFERENCE")
            return False

        for index in range(len(images)):
            coordinates = faceDetector.detectCNN(images[index])

            if coordinates != []:
                bbox = coordinates[0]
                cv2.imshow("img1", images[index])
                cv2.waitKey(25)
                # print(bbox)
                img = images[index]
                img = img[bbox[0]:bbox[2], bbox[3]:bbox[1]]

                img = cv2.resize(img, (size, size))

                cv2.imshow("img-cropped-RSZ", img)
                cv2.waitKey(25)

                new_labels.append(labels[index])
                new_images.append(img)

        print("resized ", path_load, " :", len(new_images))
        print("labels ", path_label, " :", len(new_labels))

        if save == True:
            base_label = os.path.basename(os.path.normpath(path_load))
            # base_label = base_label.replace(".npy", "")

            self.make_dirs(os.path.join(path_output, "images"))
            file_image_name = os.path.join(path_output, "images", base_label)
            print("[+] File Saving: ", file_image_name)
            np.save(file_image_name, new_images)

            base_label = os.path.basename(os.path.normpath(path_label))
            # base_label = base_label.replace(".npy", "")

            self.make_dirs(os.path.join(path_output, "labels"))
            file_label_name = os.path.join(path_output, "labels",  base_label)
            print("[+] File Saving: ", file_label_name)
            np.save(file_label_name, new_labels)


        return len(images)

    def save_images_labels_size(self, size, faceDetector, path_output):
        # images_paths, labels_paths = getDataAndLabelsPath()
        # images = []
        # labels = []
        #
        # # for path in enumerate(paths):
        # for path in labels_paths:
        #     label = np.load(path).tolist()
        #     labels += label
        #     print("len_label: ", len(label))
        # print("len: ", len(labels))

        # self.generate_labels(save=True, path_output=path_output)
        self.generate_images_with_size(size, save=True, faceDetector=faceDetector, path_output=path_output)

    def make_dirs(self, path):
        if os.path.exists(path) == False:
            os.makedirs(path)
