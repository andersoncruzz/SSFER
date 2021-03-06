import cv2
import numpy as np
from utils.constants import getDataPath
from utils.constants import getDataAndLabelsPath
from utils.constants import getLabelsPath
import os

class PreProcessing:

    def load_base_input_experiment(self, path):
        pwd = os.path.join(path, "training")
        CIFE_TR_DATA = np.load(os.path.join(pwd, 'CIFE-data-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(pwd, 'CIFE-data-ts.npy'))
        CK_DATA = np.load(os.path.join(pwd, 'ck+-data.npy'))
        FER_DATA = np.load(os.path.join(pwd, 'fer_data.npy'))
        JAFFE_DATA = np.load(os.path.join(pwd, 'JAFFE-data.npy'))
        KDEF_DATA = np.load(os.path.join(pwd, 'KDEF-data.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(pwd, 'novaemotions-data.npy'))
        RAFD_DATA = np.load(os.path.join(pwd, 'RafD-data.npy'))

        x_train = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        pwd = os.path.join(path, "training")
        CIFE_TR_DATA = np.load(os.path.join(pwd, 'CIFE-label-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(pwd, 'CIFE-label-ts.npy'))
        CK_DATA = np.load(os.path.join(pwd, 'ck+-label.npy'))
        FER_DATA = np.load(os.path.join(pwd, 'fer_labels.npy'))
        JAFFE_DATA = np.load(os.path.join(pwd, 'JAFFE-label.npy'))
        KDEF_DATA = np.load(os.path.join(pwd, 'KDEF-label.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(pwd, 'novaemotions-label.npy'))
        RAFD_DATA = np.load(os.path.join(pwd, 'RafD-label.npy'))

        y_train = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        pwd = os.path.join(path, "testing")
        CIFE_TR_DATA = np.load(os.path.join(pwd, 'CIFE-data-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(pwd, 'CIFE-data-ts.npy'))
        CK_DATA = np.load(os.path.join(pwd, 'ck+-data.npy'))
        FER_DATA = np.load(os.path.join(pwd, 'fer_data.npy'))
        JAFFE_DATA = np.load(os.path.join(pwd, 'JAFFE-data.npy'))
        KDEF_DATA = np.load(os.path.join(pwd, 'KDEF-data.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(pwd, 'novaemotions-data.npy'))
        RAFD_DATA = np.load(os.path.join(pwd, 'RafD-data.npy'))

        x_test = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        pwd = os.path.join(path, "testing")
        CIFE_TR_DATA = np.load(os.path.join(pwd, 'CIFE-label-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(pwd, 'CIFE-label-ts.npy'))
        CK_DATA = np.load(os.path.join(pwd, 'ck+-label.npy'))
        FER_DATA = np.load(os.path.join(pwd, 'fer_labels.npy'))
        JAFFE_DATA = np.load(os.path.join(pwd, 'JAFFE-label.npy'))
        KDEF_DATA = np.load(os.path.join(pwd, 'KDEF-label.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(pwd, 'novaemotions-label.npy'))
        RAFD_DATA = np.load(os.path.join(pwd, 'RafD-label.npy'))

        y_test = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        return x_train, y_train, x_test, y_test

    def load_base_for_validation(self, path):
        CIFE_TR_DATA = np.load(os.path.join(path, 'CIFE-data-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(path, 'CIFE-data-ts.npy'))
        CK_DATA = np.load(os.path.join(path, 'ck+-data.npy'))
        FER_DATA = np.load(os.path.join(path, 'fer_data.npy'))
        JAFFE_DATA = np.load(os.path.join(path, 'JAFFE-data.npy'))
        KDEF_DATA = np.load(os.path.join(path, 'KDEF-data.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(path, 'novaemotions-data.npy'))
        RAFD_DATA = np.load(os.path.join(path, 'RafD-data.npy'))

        x = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        CIFE_TR_DATA = np.load(os.path.join(path, 'CIFE-label-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(path, 'CIFE-label-ts.npy'))
        CK_DATA = np.load(os.path.join(path, 'ck+-label.npy'))
        FER_DATA = np.load(os.path.join(path, 'fer_labels.npy'))
        JAFFE_DATA = np.load(os.path.join(path, 'JAFFE-label.npy'))
        KDEF_DATA = np.load(os.path.join(path, 'KDEF-label.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(path, 'novaemotions-label.npy'))
        RAFD_DATA = np.load(os.path.join(path, 'RafD-label.npy'))

        y = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        return x, y



    def load_base(self, path):
        pwd = os.path.join(path, "images")
        CIFE_TR_DATA = np.load(os.path.join(pwd, 'CIFE-data-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(pwd, 'CIFE-data-ts.npy'))
        CK_DATA = np.load(os.path.join(pwd, 'ck+-data.npy'))
        FER_DATA = np.load(os.path.join(pwd, 'fer_data.npy'))
        JAFFE_DATA = np.load(os.path.join(pwd, 'JAFFE-data.npy'))
        KDEF_DATA = np.load(os.path.join(pwd, 'KDEF-data.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(pwd, 'novaemotions-data.npy'))
        RAFD_DATA = np.load(os.path.join(pwd, 'RafD-data.npy'))

        images = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        pwd = os.path.join(path, "labels")
        CIFE_TR_DATA = np.load(os.path.join(pwd, 'CIFE-label-tr.npy'))
        CIFE_TS_DATA = np.load(os.path.join(pwd, 'CIFE-label-ts.npy'))
        CK_DATA = np.load(os.path.join(pwd, 'ck+-label.npy'))
        FER_DATA = np.load(os.path.join(pwd, 'fer_labels.npy'))
        JAFFE_DATA = np.load(os.path.join(pwd, 'JAFFE-label.npy'))
        KDEF_DATA = np.load(os.path.join(pwd, 'KDEF-label.npy'))
        NOVAEMOTIONS_DATA = np.load(os.path.join(pwd, 'novaemotions-label.npy'))
        RAFD_DATA = np.load(os.path.join(pwd, 'RafD-label.npy'))

        labels = np.concatenate((CIFE_TR_DATA, CIFE_TS_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA), axis=0)

        return images, labels


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

    def validateCoordinate(self, coordinate, size):
        #print(coordinate)
        #print("size: ", type(size))
        coordinate = list(coordinate)
        if coordinate[0] > size:
            coordinate[0] = size
        if coordinate[1] > size:
            coordinate[1] = size
        if coordinate[2] > size:
            coordinate[2] = size
        if coordinate[3] > size:
            coordinate[3] = size

        if coordinate[0] < 0:
            coordinate[0] = 0
        if coordinate[1] < 0:
            coordinate[1] = 0
        if coordinate[2] < 0:
            coordinate[2] = 0
        if coordinate[3] < 0:
            coordinate[3] = 0

        return tuple(coordinate)


    def resize_all_images_label(self, size, path_load, path_output, path_label, faceDetector=None, save=True):
        #TODO: Verify others possible resize processing, cubic, linear, etc, upsample
        new_images = []
        new_labels = []

        images = np.load(path_load)
        labels = np.load(path_label)

        #print("[+] SIZE: ", size)

        if len(images) != len(labels):
            print("[+] ERROR LABEL AND IMAGE SIZE DIFFERENCE")
            return False

        for index in range(len(images)):
            coordinates = faceDetector.detectMTCNN(images[index])

            if coordinates != []:
                bbox = coordinates[0]
                # cv2.imshow("img1", images[index])
                # cv2.waitKey(25)
                #print(index)
                #print(bbox)
                img = images[index]
                #print(img.shape)
                bbox = self.validateCoordinate(bbox, img.shape[0])
                img = img[bbox[0]:bbox[2], bbox[3]:bbox[1]]

                img = cv2.resize(img, (size, size))

                cv2.imshow("img-cropped-RSZ", img)
                cv2.waitKey(10)

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


        return len(new_images)

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
