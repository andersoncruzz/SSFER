import os
import numpy as np


def make_dirs(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

data_path = ["CIFE-data-tr.npy", "ck+-data.npy", "JAFFE-data.npy", "novaemotions-data.npy",
                "CIFE-data-ts.npy", "fer_data.npy", "KDEF-data.npy", "RafD-data.npy"]


label_path = ["CIFE-label-tr.npy", "ck+-label.npy", "JAFFE-label.npy", "novaemotions-label.npy" ,
                "CIFE-label-ts.npy", "fer_labels.npy", "KDEF-label.npy", "RafD-label.npy"]

path_input_base_name = "output_60"
path_output_base_name = "split_dbs_original_at"

if len(data_path) != len(label_path):
    print("[+] ERROR SIZE DATA AND LABEL ARE DIFFERENT")
    exit()

counter_classes = [0, 0, 0, 0, 0, 0, 0, 0]

for item in range(len(data_path)):
    data = np.load(os.path.join(path_input_base_name, "images", data_path[item]))
    label = np.load(os.path.join(path_input_base_name, "labels", label_path[item]))

    print("database data: ", os.path.join(path_input_base_name, "images", data_path[item]))
    print("database label: ", os.path.join(path_input_base_name, "labels", label_path[item]))
    
    dataset_train_data = []
    dataset_test_data = []
    dataset_validation_data = []

    dataset_train_label = []
    dataset_test_label = []
    dataset_validation_label = []


    counter_classes_train = [0, 0, 0, 0, 0, 0, 0, 0]
    counter_classes_test = [0, 0, 0, 0, 0, 0, 0, 0]
    counter_classes_validation = [0, 0, 0, 0, 0, 0, 0, 0]

    flags = [0, 0, 0, 0, 0, 0, 0, 0]

    if len(data) != len(label):
        print("[+] ERROR")
        exit()

    print("size images: ", len(data))
    for i in range(len(data)):
        emotion_index = np.argmax(label[i])
        counter_classes[emotion_index] += 1

        if flags[emotion_index] == 0 or flags[emotion_index] == 2:
            dataset_train_data.append(data[i])
            dataset_train_label.append(emotion_index)
            flags[emotion_index] += 1
            counter_classes_train[emotion_index] += 1

        elif flags[emotion_index] == 1:
            dataset_test_data.append(data[i])
            dataset_test_label.append(emotion_index)
            flags[emotion_index] += 1
            counter_classes_test[emotion_index] += 1

        elif flags[emotion_index] == 3:
            dataset_validation_data.append(data[i])
            dataset_validation_label.append(emotion_index)
            flags[emotion_index] = 0
            counter_classes_validation[emotion_index] += 1

    print("counter_classes: ", counter_classes)
    print("counter_classes_train: ", counter_classes_train)
    print("counter_classes_test: ", counter_classes_test)
    print("counter_classes_validation: ", counter_classes_validation)
    print("size of dataset_train_data: ", len(dataset_train_data))
    print("size of dataset_test_data: ", len(dataset_test_data))
    print("size of dataset_validation_data: ", len(dataset_validation_data))
    print("-----------------------------------")
