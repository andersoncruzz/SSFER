#EXPERIMENTO VGG16 IMG_SIZE 60, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 0 --batch_size 7
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 0 --batch_size 14
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 0 --batch_size 21
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 0 --batch_size 28
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 0 --batch_size 35

#EXPERIMENTO VGG19 IMG_SIZE 60, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 7
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 14
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 21
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 28
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 1 --batch_size 35


#EXPERIMENTO MobileNet IMG_SIZE 60, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 2 --batch_size 7
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 2 --batch_size 14
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 2 --batch_size 21
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 2 --batch_size 28
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 2 --batch_size 35

#EXPERIMENTO MobileNetV2 IMG_SIZE 60, lr 0.1 Adadelta variando o batch_size
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 3 --batch_size 7
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 3 --batch_size 14
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 3 --batch_size 21
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 3 --batch_size 28
python train_classifiers.py --img_size 60  --learning_rate 0.1 \
                            --optimizer 0 --architecture 3 --batch_size 35
