import keras.applications as classifiers


class ResNet50:
    def build_network(self, input_shape, num_classes):
        model = classifiers.resnet50.ResNet50(include_top=True,
                                        input_shape=input_shape
                                        weights=None,
                                        input_tensor=None,
                                        input_shape=None,
                                        pooling='max',
                                        classes=num_classes)
        return model
