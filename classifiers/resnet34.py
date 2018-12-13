import keras_contrib.applications.resnet as resnet


class ResNet34:
    def build_network(self, input_shape, num_classes):
        model = resnet.ResNet34(input_shape=input_shape, classes=num_classes)
        return model
