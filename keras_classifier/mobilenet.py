import keras.applications as classifiers


class MobileNet:
    def build_network(self, input_shape, num_classes):
        model = classifiers.mobilenet.MobileNet(input_shape=input_shape,
                                                alpha=1.0,
                                                depth_multiplier=1,
                                                dropout=1e-3,
                                                include_top=True,
                                                weights=None,
                                                input_tensor=None,
                                                pooling='max',
                                                classes=num_classes)
        return model
