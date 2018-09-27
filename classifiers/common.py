import keras
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
import os

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
