import keras
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
import os
import cv2
import numpy as np


def train(model, x_train, y_train, x_test, y_test, batch_size, epochs, path_dir, split):
    try:
        os.mkdir(path_dir)
    except:
        pass

    filepath = os.path.join(path_dir, "weights.{epoch:02d}-{val_loss:.2f}.hdf5")
    checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]

    model.fit(x_train, y_train,
                  batch_size = batch_size,
                  epochs = epochs,
                  verbose = 2,
                  shuffle = True,
                  validation_split = split,
                  # validation_data=(x_test, y_test),
                  callbacks = callbacks_list)

    return model

def evaluate(model, x_test, y_test):
    score = model.evaluate(x_test, y_test, verbose=0)
    return score

def compile_net(model):
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
    return model

def add_last_layer(model, num_classes):
    model.add(Dense(num_classes, activation='softmax', name='predictions'))
    return model

def load_model_net(path):
    model = load_model(path)
    return model

def classify_image(model, img):
    return model.predict([img])

def classify_image_from_path(model, path):
    img = cv2.imread(path)
    img = np.array(img)
    img = img.reshape(1, 80, 80, 3)

    print("shape: ", img.shape)
    return model.predict([np.array(img)])

def classify_bath_image_from_path(model, path, clazz):
    cont = [0, 0]
    for file in os.listdir(path):
        img = cv2.imread(os.path.join(path, file))
        img = np.array(img)
        img = img.reshape(1, 80, 80, 3)

        # print("shape: ", img.shape)
        vet = model.predict([np.array(img)])
        print("vet: ", vet)
        if np.argmax(vet[0]) == clazz:
            cont[0] += 1
        else:
            cont[1] += 1
    print("Classe: ", clazz, " Conts: ", cont)
