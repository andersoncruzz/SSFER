
def train(model, x_train, y_train, x_test, y_test, batch_size, epochs):
    model.fit(x_train, y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  verbose=1,
                  validation_data=(x_test, y_test))
    return model

def evaluate(model, x_test, y_test):
    score = model.evaluate(x_test, y_test, verbose=0)
    return score
