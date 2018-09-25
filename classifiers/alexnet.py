'''Trains a simple convnet on the MNIST dataset.
Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''

from __future__ import print_function
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
# from keras import backend as K
import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
# K.set_image_dim_ordering('th')
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.87
set_session(tf.Session(config=config))

class Alexnet:
    def build_network(self, input_shape, num_classes):
        print("INPUT_SHAPE: ", input_shape)
        model = Sequential()
        model.add(Conv2D(96, kernel_size = (11, 11),
                         activation='relu',
                         padding='same',
                         input_shape=input_shape))
        model.add(MaxPooling2D(pool_size=(3, 3)))

        model.add(Conv2D(256, kernel_size = (5, 5),
                        padding='same',
                        activation='relu'))
        model.add(MaxPooling2D(pool_size=(3, 3)))

        # model.add(Conv2D(384, kernel_size = (3, 3),
        #                 padding='same',
        #                 activation='relu'))
        # model.add(Conv2D(384, kernel_size = (3, 3),
        #                 padding='same',
        #                 activation='relu'))
        model.add(Conv2D(256, kernel_size = (3, 3),
                        padding='same',
                        activation='relu'))

        # model.add(Dropout(0.5))
        model.add(Flatten())
        model.add(Dense(4096, activation='relu'))
        model.add(Dense(4096, activation='relu'))

        return model
