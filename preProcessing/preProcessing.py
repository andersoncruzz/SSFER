import cv2
import numpy as np
from utils.constants import getDataPath

class PreProcessing:

    def loadAllImagesWithSize(self, size, save=False):
        # CIFE_DATA, CK_DATA, FER_DATA, JAFFE_DATA, KDEF_DATA, NOVAEMOTIONS_DATA, RAFD_DATA = getDataPath()
        paths = getDataPath()
        images = []
        for path in paths:
            print("path: ", path)
            images += self.resizeAllImages(np.load(path), size, path)

        if save == True:
            np.save("image_size_"+str(size[0])+"_.npy", images)
        return images

    def loadFromFile(self, path):
        return np.load(path)

    def resizeAllImages(self, images, size, path):
        #TODO: Verify others possible resize processing, cubic, linear, etc, upsample
        new_images = []
        for img in images:
            new_images.append(cv2.resize(img, size))
        print("resized ", path, " :", len(new_images))
        return new_images
