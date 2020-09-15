import os     
# os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" 
# os.environ["CUDA_VISIBLE_DEVICES"]="-1"    
# os.environ["PATH"] += os.pathsep + 'E:/system/python/graphviz/bin'
import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt

import random

from keras.callbacks import TensorBoard
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout, Lambda,Conv2D,MaxPooling2D
from keras.optimizers import RMSprop
from keras import backend as K
from keras import regularizers
from resnet_keras import *
from vgg_16_keras import *
from simplemodel_keras import *
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator


def euclidean_distance(vects):
    x, y = vects
    sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
    return K.sqrt(K.maximum(sum_square, K.epsilon()))


def manhattan_distance(vects):
    x, y = vects
    sum_square = K.sum(K.abs(x - y))
    return K.maximum(sum_square, K.epsilon())

def cosine_distance(vects):
    x, y = vects
    x = K.l2_normalize(x, axis=-1)
    y = K.l2_normalize(y, axis=-1)
    sum_square=K.sum(x * y, axis=-1, keepdims=True)
    return K.maximum(sum_square, K.epsilon())


def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)


def contrastive_loss(y_true, y_pred):
    '''Contrastive loss from Hadsell-et-al.'06
    http://yann.lecun.com/exdb/publis/pdf/hadsell-chopra-lecun-06.pdf
    '''
    margin = 1
    sqaure_pred = K.square(y_pred)
    margin_square = K.square(K.maximum(margin - y_pred, 0))
    return K.mean(y_true * sqaure_pred + (1 - y_true) * margin_square)




def compute_accuracy(y_true, y_pred): # numpy上的操作
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    pred = y_pred.ravel() < 0.5
    return np.mean(pred == y_true)


def accuracy(y_true, y_pred): # Tensor上的操作
    '''Compute classification accuracy with a fixed threshold on distances.
    '''
    return K.mean(K.equal(y_true, K.cast(y_pred < 0.5, y_true.dtype)))

def plot_train_history(history, train_metrics, val_metrics):
    plt.plot(history.history.get(train_metrics), '-o')
    plt.plot(history.history.get(val_metrics), '-o')
    plt.ylabel(train_metrics)
    plt.xlabel('Epochs')
    plt.legend(['train', 'validation'])

def create_pairs(x, digit_indices,num_classes):
    '''Positive and negative pair creation.
    Alternates between positive and negative pairs.
    '''
    pairs = []
    labels = []
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        for i in range(n):
            z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
            pairs += [[x[z1], x[z2]]]
            inc = random.randrange(1, num_classes)
            dn = (d + inc) % num_classes
            z1, z2 = digit_indices[d][i], digit_indices[dn][i]
            pairs += [[x[z1], x[z2]]]
            labels += [1, 0]
    return np.array(pairs), np.array(labels)
    
def create_pairs_incre_1(x, digit_indices,num_classes):
    pairs = []
    labels = []
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        n=len(digit_indices[d])-1
        for i in range(n):
            for j in range(i+1,n+1):
                z1, z2 = digit_indices[d][i], digit_indices[d][j]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j)
                inc_1 = np.random.randint(1, num_classes)
                dn = (d + inc_1) % num_classes
                inc_2 =np.random.randint(0, len(digit_indices[dn]))
                z1, z2 = digit_indices[d][i], digit_indices[dn][inc_2]
                pairs += [[x[z1], x[z2]]]

                labels += [1, 0]

    return np.array(pairs), np.array(labels)


def create_pairs_incre_2(x, digit_indices,num_classes):
    '''Positive and negative pair creation.
    Alternates between positive and negative pairs.
    '''
    pairs = []
    labels = []
    print([len(digit_indices[d]) for d in range(num_classes)])
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        for i in range(n):
            for j in range(i+1,n+1):
                z1, z2 = digit_indices[d][i], digit_indices[d][j]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*2)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*3)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*4)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*5)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                labels += [1, 0, 0, 0, 0, 0]

    return np.array(pairs), np.array(labels)


def create_siamese_network(input_shape):
	       
    # base_network = simplemoel_mlp(input_shape)
    base_network = simplemoel_mlp(input_shape)
    # base_network = simplemoel_conv(input_shape)
    # base_network = ResNet50(input_shape,128)
    # base_network = vgg_16_base(input_shape,128)


    input_a = Input(shape=input_shape)
    input_b = Input(shape=input_shape)
	# because we re-use the same instance `base_network`,
	# the weights of the network
	# will be shared across the two branches
    processed_a = base_network(input_a)
    processed_b = base_network(input_b)
    distance = Lambda(euclidean_distance,output_shape=eucl_dist_output_shape)([processed_a, processed_b])

    model = Model([input_a, input_b], distance)
	# keras.utils.plot_model(model,"siamModel.png",show_shapes=True)
    model.summary()

	# train
    rms = RMSprop()
    model.compile(loss=contrastive_loss, optimizer=rms, metrics=[accuracy])
    return model


def siamese_accuracy_score(target,scores,threshold):#目标，结果，第i个对象是正确对象
    tp=0
    tn=0
    fp=0
    fn=0

    for j in range(len(scores)):

        if scores[j]<threshold:
            if target[j]==1:
                tp=tp+1
            else:
                fp=fp+1
        else:
            if target[j]==1:
                fn=fn+1
            else:
                tn=tn+1
    return tp,tn,fp,fn

num_classes = 10
epochs = 50

# the data, split between train and test sets
(train_data, train_target), (test_data, test_target) = mnist.load_data()
train_data = train_data.astype('float32')
test_data = test_data.astype('float32')
train_data /= 255
test_data /= 255
input_shape = train_data.shape[1:]


# datagen = ImageDataGenerator(zoom_range=3)

# datagen.fit(train_data)



# create training+test positive and negative pairs
digit_indices = [np.where(train_target == i)[0] for i in range(0,num_classes)]
train_pairs, train_label = create_pairs(train_data, digit_indices,num_classes)

digit_indices = [np.where(test_target == i)[0] for i in range(0,num_classes)]
test_pairs, test_label = create_pairs(test_data, digit_indices,num_classes)


input_shape = (28,28,1)
train_pairs = train_pairs.reshape(train_pairs.shape[0], 2, 28, 28, 1)  
test_pairs = test_pairs.reshape(test_pairs.shape[0], 2, 28, 28, 1) 
print(train_pairs.shape)
print(test_pairs.shape)


# 自定义层
model=create_siamese_network(input_shape)
train_pairs,val_pairs, train_label, val_label = train_test_split(train_pairs,train_label,test_size = 0.2,random_state = 30,stratify=train_label)

train_pairs = train_pairs.astype(np.float32)
val_pairs = val_pairs.astype(np.float32)
test_pairs = test_pairs.astype(np.float32)
train_label = train_label.astype(np.float32)
val_label = val_label.astype(np.float32)
test_label = test_label.astype(np.float32)


# history=model.fit([train_data[:, 0], train_data[:, 1]], train_target,
#           batch_size=128,
#           epochs=epochs,verbose=2,
#           validation_split=0.2)

history=model.fit([train_pairs[:, 0], train_pairs[:, 1]], train_label,
          batch_size=128,
          epochs=epochs,verbose=2,
          validation_data=([val_pairs[:, 0], val_pairs[:, 1]], val_label))
# history = model.fit([train_pairs[:, 0], train_pairs[:, 1]], train_label,  
#            batch_size=128,  
#            epochs=epochs, verbose=2,
#            validation_data=([test_pairs[:, 0], test_pairs[:, 1]], test_label))  


# plt.figure(figsize=(8, 4))
# plt.subplot(1, 2, 1)
# plot_train_history(history, 'loss', 'val_loss')
# plt.subplot(1, 2, 2)
# plot_train_history(history, 'accuracy', 'val_accuracy')
# plt.show()


# compute final accuracy on training and test sets
y_pred = model.predict([train_pairs[:, 0], train_pairs[:, 1]])
tr_acc = compute_accuracy(train_label, y_pred)
y_pred = model.predict([test_pairs[:, 0], test_pairs[:, 1]])
te_acc = compute_accuracy(test_label, y_pred)

print('* Accuracy on training set: %0.2f%%' % (100 * tr_acc))
print('* Accuracy on test set: %0.2f%%' % (100 * te_acc))


i=0.1
while i<2:
    tp,tn,fp,fn=siamese_accuracy_score(test_label,y_pred,i)
    print(tp,tn,fp,fn)
    accuracy=(tp+tn)/(tp+tn+fp+fn)
    far=(fp)/(fp+tn)
    frr=(fn)/(fn+tp)
    print("i=",i)
    print("accuracy:",accuracy,"far:",far,"frr:",frr)
    i=i+0.1