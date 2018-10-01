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

# from keras.backend.tensorflow_backend import set_session
# # K.set_image_dim_ordering('th')
# config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.95
# set_session(tf.Session(config=config))

class Vgg:
    def build_network(self, input_shape, num_classes):
        print("INPUT_SHAPE: ", input_shape)
        model = Sequential()
        model.add(Conv2D(64, kernel_size = (3, 3),
                         activation='relu',
                         padding='same',
                         name='block1_conv1',
                         input_shape=input_shape))
        model.add(Conv2D(64, kernel_size = (3, 3),
                        padding='same',
                        name='block1_conv2',
                        activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),
                                strides=(2,2),
                                name='block1_pool'))


        model.add(Conv2D(128, kernel_size = (3, 3),
                         activation='relu',
                         padding='same',
                         name='block2_conv1',
                         input_shape=input_shape))
        model.add(Conv2D(128, kernel_size = (3, 3),
                        padding='same',
                        name='block2_conv2',
                        activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),
                                strides=(2,2),
                                name='block2_pool'))


        model.add(Conv2D(256, kernel_size = (3, 3),
                         activation='relu',
                         padding='same',
                         name='block3_conv1',
                         input_shape=input_shape))
        model.add(Conv2D(256, kernel_size = (3, 3),
                        padding='same',
                        name='block3_conv2',
                        activation='relu'))
        model.add(Conv2D(256, kernel_size = (3, 3),
                        padding='same',
                        name='block3_conv3',
                        activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),
                                strides=(2,2),
                                name='block3_pool'))


        model.add(Conv2D(512, kernel_size = (3, 3),
                         activation='relu',
                         padding='same',
                         name='block4_conv1',
                         input_shape=input_shape))
        model.add(Conv2D(512, kernel_size = (3, 3),
                        padding='same',
                        name='block4_conv2',
                        activation='relu'))
        model.add(Conv2D(512, kernel_size = (3, 3),
                        padding='same',
                        name='block4_conv3',
                        activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),
                                strides=(2,2),
                                name='block4_pool'))


        model.add(Conv2D(512, kernel_size = (3, 3),
                         activation='relu',
                         padding='same',
                         name='block5_conv1',
                         input_shape=input_shape))
        model.add(Conv2D(512, kernel_size = (3, 3),
                        padding='same',
                        name='block5_conv2',
                        activation='relu'))
        model.add(Conv2D(512, kernel_size = (3, 3),
                        padding='same',
                        name='block5_conv3',
                        activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2),
                                strides=(2,2),
                                name='block5_pool'))


        # model.add(Dropout(0.5))
        model.add(Flatten(name='flatten'))
        model.add(Dense(4096, activation='relu', name='fc1'))
        model.add(Dense(4096, activation='relu', name='fc2'))

        return model
