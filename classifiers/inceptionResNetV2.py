import keras.applications as classifiers


class InceptionResNetV2:
    def build_network(self, input_shape, num_classes):
        model = classifiers.inception_resnet_v2.InceptionResNetV2(include_top=True,
                                        weights=None,
                                        input_tensor=None,
                                        input_shape=input_shape,
                                        pooling='max',
                                        classes=num_classes)
        return model
