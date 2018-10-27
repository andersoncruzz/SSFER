from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D

class NetSimple:
    # def build_network(self, input_shape, num_classes):
    #     model = Sequential()
    #     model.add(Conv2D(16, kernel_size=(3, 3),
    #                 activation='relu',
    #                 input_shape=input_shape))
    #     model.add(Conv2D(32, (3, 3), activation='relu'))
    #     model.add(MaxPooling2D(pool_size=(2, 2)))
    #     model.add(Flatten())
    #     model.add(Dense(64, activation='relu'))
    #     model.add(Dropout(0.25))
    #     model.add(Dense(num_classes, activation='softmax'))
    #     return model

    def build_network(self, input_shape, num_classes):
        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3), padding='same',
                    activation='relu',
                    input_shape=input_shape))
        model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
        model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
        model.add(MaxPooling2D(pool_size=(2, 2)))


        model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
        model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        # model.add(Dropout(0.25))
        model.add(Flatten())

        model.add(Dense(1000, activation='relu'))
        model.add(Dense(1000, activation='relu'))
        # model.add(Dropout(0.25))

        model.add(Dense(num_classes, activation='softmax'))
        return model
