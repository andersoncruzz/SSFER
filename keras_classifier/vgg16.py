import keras.applications as classifiers


class VGG16:
    def build_network(self, input_shape, num_classes):
        model = classifiers.vgg16.VGG16(include_top=True,
                                        input_shape=input_shape,
                                        weights=None,
                                        input_tensor=None,
                                        pooling='max',
                                        classes=num_classes)
        return model
