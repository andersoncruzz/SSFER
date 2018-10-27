import keras
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from keras.models import load_model
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class Common:

    def save_plot_losses(self, history, path_dir):
        plt.figure(figsize=[8,6])
        plt.plot(history.history['loss'],'r',linewidth=3.0)
        plt.plot(history.history['val_loss'],'b',linewidth=3.0)
        plt.legend(['Custo no Treino', 'Custo no Teste'],fontsize=18)
        plt.xlabel('Épocas ',fontsize=16)
        plt.ylabel('Custo',fontsize=16)
        plt.title('Curvas da Função de Custo',fontsize=16)
        plt.savefig(os.path.join(path_dir, 'loss.png'))

    def save_plot_acc(self, history, path_dir):
        plt.figure(figsize=[8,6])
        plt.plot(history.history['acc'],'r',linewidth=3.0)
        plt.plot(history.history['val_acc'],'b',linewidth=3.0)
        plt.legend(['Acurácia no Treino', 'Acurácia no Teste'],fontsize=18)
        plt.xlabel('Épocas ',fontsize=16)
        plt.ylabel('Acurácia',fontsize=16)
        plt.title('Curvas da Acurácia',fontsize=16)
        plt.savefig(os.path.join(path_dir, 'acc.png'))

    def write_file_info(self, path_dir, content):
        file_info_path = os.path.join(path_dir, "info.txt")
        file_info_experiment = open(file_info_path, "a+")

        for i in content:
            line = str(i) + "\n"
            file_info_experiment.write(line)

        file_info_experiment.close()

    def train(self, model, x_train, y_train, x_test, y_test, batch_size, epochs, path_dir):
        self.write_file_info(path_dir, ["batch_size: "+str(batch_size)])

        file_weights = os.path.join(path_dir, "weights.{epoch:02d}-{val_loss:.2f}.hdf5")
        checkpoint = ModelCheckpoint(file_weights, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')
        # checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
        earlystopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=20, verbose=1, mode='auto')

        callbacks_list = [checkpoint, earlystopping]

        history = model.fit(x_train, y_train,
                      batch_size = batch_size,
                      epochs = epochs,
                      verbose = 1,
                      shuffle = True,
                      validation_data=(x_test, y_test),
                      callbacks = callbacks_list)

        return model, history

    def evaluate(self, model, x_test, y_test):
        score = model.evaluate(x_test, y_test, verbose=0)
        return score

    def compile_net(self, model, path_dir, learning_rate, option):
        self.write_file_info(path_dir, ["learning_rate: "+str(learning_rate), "optimizer: " + str(option)])

        if option == "Adadelta":
            model.compile(loss=keras.losses.categorical_crossentropy,
                          optimizer=keras.optimizers.Adadelta(lr=learning_rate),
                          # optimizer=keras.optimizers.SGD(lr=learning_rate),
                          # optimizer=keras.optimizers.Nadam(lr=learning_rate),
                          # optimizer=keras.optimizers.RMSprop(lr=learning_rate),
                          metrics=['accuracy'])

        elif option == "SGD":
            model.compile(loss=keras.losses.categorical_crossentropy,
                          # optimizer=keras.optimizers.Adadelta(lr=learning_rate),
                          optimizer=keras.optimizers.SGD(lr=learning_rate),
                          # optimizer=keras.optimizers.Nadam(lr=learning_rate),
                          # optimizer=keras.optimizers.RMSprop(lr=learning_rate),
                          metrics=['accuracy'])

        elif option == "Nadam":
            model.compile(loss=keras.losses.categorical_crossentropy,
                          # optimizer=keras.optimizers.Adadelta(lr=learning_rate),
                          # optimizer=keras.optimizers.SGD(lr=learning_rate),
                          optimizer=keras.optimizers.Nadam(lr=learning_rate),
                          # optimizer=keras.optimizers.RMSprop(lr=learning_rate),
                          metrics=['accuracy'])

        elif option == "RMSprop":
            model.compile(loss=keras.losses.categorical_crossentropy,
                          # optimizer=keras.optimizers.Adadelta(lr=learning_rate),
                          # optimizer=keras.optimizers.SGD(lr=learning_rate),
                          # optimizer=keras.optimizers.Nadam(lr=learning_rate),
                          optimizer=keras.optimizers.RMSprop(lr=learning_rate),
                          metrics=['accuracy'])


        return model

    def load_model_net(self, path):
        model = load_model(path)
        return model

    def classify_image(self, model, img):
        return model.predict([img])

    def classify_image_from_path(self, model, path, dim):
        img = cv2.imread(path)
        img = cv2.resize(img, (dim, dim))
        img = np.array(img)
        img = img.astype('float32')
        img = img / 255

        img = img.reshape(1, dim, dim, 3)

        print("shape: ", img.shape)
        return model.predict([np.array(img)])

    def classify_bath_image_from_path(self, model, path, clazz, dim):
        cont = [0, 0]
        # print("255")
        for file in os.listdir(path):
            img = cv2.imread(os.path.join(path, file))
            img = cv2.resize(img, (dim, dim))
            cv2.imshow("img", img)
            cv2.waitKey(200)
            img = np.array(img)
            img = img.astype('float32')
            img = img / 255

            img = img.reshape(1, dim, dim, 3)
            # print([np.array(img)])
            # print("shape: ", img.shape)
            vet = model.predict([np.array(img)])
            # print("vet: ", vet)
            if np.argmax(vet[0]) == clazz:
                cont[0] += 1
            else:
                cont[1] += 1
                print(file)
        print("Classe: ", clazz, " Conts: ", cont)
