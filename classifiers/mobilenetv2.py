import keras.applications as classifiers


class MobileNetV2:
    def build_network(self, input_shape, num_classes):
        model = classifiers.mobilenetv2.MobileNetV2(input_shape=input_shape,
                                                alpha=1.0,
                                                depth_multiplier=1,
                                                include_top=True,
                                                weights=None,
                                                input_tensor=None,
                                                pooling='max',
                                                classes=num_classes)
        return model
