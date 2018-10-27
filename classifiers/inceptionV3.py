import keras.applications as classifiers


class InceptionV3:
    def build_network(self, input_shape, num_classes):
        model = classifiers.inception_v3.InceptionV3(include_top=True,
                                        weights=None,
                                        input_tensor=None,
                                        input_shape=input_shape,
                                        pooling='max',
                                        classes=num_classes)
        return model
