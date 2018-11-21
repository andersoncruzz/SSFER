#EXPERIMENTO InceptionResNetV2 IMG_SIZE 160, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 160  --learning_rate 0.1 \
                            --optimizer 0 --architecture 6 --batch_size 7
python train_classifiers.py --img_size 160  --learning_rate 0.1 \
                            --optimizer 0 --architecture 6 --batch_size 14

#EXPERIMENTO ResNet50 IMG_SIZE 160, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 210  --learning_rate 0.1 \
                            --optimizer 0 --architecture 4 --batch_size 7
python train_classifiers.py --img_size 210  --learning_rate 0.1 \
                            --optimizer 0 --architecture 4 --batch_size 14

#EXPERIMENTO VGG19 IMG_SIZE 110, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 110  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 7
python train_classifiers.py --img_size 110  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 14
python train_classifiers.py --img_size 110  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 35

#EXPERIMENTO VGG19 IMG_SIZE 160, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 160  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 7
python train_classifiers.py --img_size 160  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 28
python train_classifiers.py --img_size 160  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 35
