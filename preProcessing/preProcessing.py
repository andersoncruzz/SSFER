import cv2
import numpy as np
from utils.constants import getDataPath
from utils.constants import getDataAndLabelsPath
from utils.constants import getLabelsPath

class PreProcessing:

    def load_images_with_size(self, size, save=False, paths=None):
        # CIFE_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA = getDataPath()
        if paths == None:
            paths = getDataPath()

        images = []
        for path in paths:
            print("path: ", path)
            images += self.resize_all_images(size, path)

        print("[+] Images Len: ", len(images))

        if save == True:
            np.save("db2/image_size_"+str(size)+"_.npy", images)
        return images

    def load_labels(self, save=False, paths=None):
        if paths == None:
            paths = getLabelsPath()

        labels = []

        # for path in enumerate(paths):
        for path in paths:
            label = np.load(path).tolist()
            labels += label

        print("[+] Labels len: ", len(labels))

        if save == True:
            np.save("db2/labels.npy", labels)

        return labels

    def load_from_file(self, path):
        return np.load(path)

    def resize_all_images(self, size, path):
        #TODO: Verify others possible resize processing, cubic, linear, etc, upsample
        new_images = []
        images = np.load(path)

        for img in images:
            new_images.append(cv2.resize(img, (size, size)))
        print("resized ", path, " :", len(new_images))
        return new_images

    def save_images_labels_size(self, size, save=False):
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
        self.load_labels(save=True)
        self.load_images_with_size(70, save=True)
