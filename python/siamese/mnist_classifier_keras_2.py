import os
from tensorflow.keras.layers import Input
import tensorflow as tf
from tensorflow.keras.models import Model

from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.layers import concatenate, Lambda, Embedding
import tensorflow.keras.backend as K
import numpy as np
from tensorflow.keras.callbacks import TensorBoard
import os
from keras.datasets import mnist
from itertools import permutations
import random
from tensorflow.keras.layers import Input, Dense, Flatten, BatchNormalization,Conv2D, MaxPooling2D, ReLU,Dropout
from keras import regularizers,optimizers

def simplemoel_mlp(input):
    '''Base network to be shared (eq. to feature extraction).
    '''
    x = Flatten()(input)
    #全连接层
    x = Dense(128, activation='relu')(x)
    #遗忘层
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    pre_logit = Dense(128, activation='relu')(x)

    softmax = Dense(10, activation='softmax')(pre_logit)
    return softmax, pre_logit


def generate_pair(x, y):
    num_classes=len(set(y))
    digit_indices = [np.where(y == i)[0] for i in range(0,num_classes)]
    pairs = []
    labels = []
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        for i in range(n):
            z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
            pairs.append([x[z1], x[z2]])
            labels.append([d,d])
            
            inc = random.randrange(1, num_classes)
            dn = (d + inc) % num_classes
            z1, z2 = digit_indices[d][i], digit_indices[dn][i]
            pairs.append([x[z1], x[z2]])
            labels.append([d,dn])
    return np.array(pairs), np.array(labels)

def contrastive_loss(y_true, y_pred):
    """
    Implementation of the triplet loss function
    Arguments:
    y_true -- true labels, required when you define a loss in Keras, you don't need it in this function.
    y_pred -- python list containing three objects:
            anchor -- the encodings for the anchor data
            positive -- the encodings for the positive data (similar to anchor)
            negative -- the encodings for the negative data (different from anchor)
    Returns:
    loss -- real number, value of the loss
    """
    print('y_pred.shape = ', y_pred)
    total_lenght = y_pred.shape.as_list()[-1]

    anchor_1_pred = y_pred[:, 0:int(total_lenght * 1 / 2)]
    anchor_2_pred = y_pred[:, int(total_lenght * 1 / 2):int(total_lenght * 2 / 2)]

    anchor_1_true = y_true[:, 0:int(total_lenght * 1 / 2)]
    anchor_2_true = y_true[:, int(total_lenght * 1 / 2):int(total_lenght * 2 / 2)]

    # distance between the anchor and the positive
    pos_dist = K.sqrt(K.sum(K.square(anchor_1_pred - anchor_2_pred), axis=1))
    
    margin = 1

    sqaure_pred = K.square(pos_dist)
    margin_square = K.square(K.maximum(margin - pos_dist, 0))

    # compute loss
    true_combine=y_true[:, 0:int(total_lenght * 1 / 2)]-y_true[:, int(total_lenght * 1 / 2):int(total_lenght * 2 / 2)]


    loss = K.mean(true_combine * sqaure_pred + (1 - true_combine) * margin_square)

    return loss

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

(train_data, train_target), (test_data, test_target) = mnist.load_data()
train_data = train_data.astype('float32')
test_data = test_data.astype('float32')
train_data /= 255
test_data /= 255

model_input = Input(shape=(28, 28, 1))
softmax, pre_logits = simplemoel_mlp(model_input)

X_train, Y_train = generate_pair(train_data, train_target)
shared_model = Model(inputs=[model_input], outputs=[softmax, pre_logits])

input_a = Input((28, 28, 1), name='input_a')
input_b = Input((28, 28, 1), name='input_b')

soft_a, pre_logits_a = shared_model([input_a])
soft_b, pre_logits_b = shared_model([input_b])

merged_soft = concatenate([soft_a, soft_b], axis=-1, name='merged_soft')
merged_pre = concatenate([pre_logits_a, pre_logits_b], axis=-1, name='merged_pre')

model = Model(inputs=[input_a, input_b], outputs=[merged_soft, merged_pre])
model.summary()
rms = optimizers.RMSprop()
model.compile(loss=["categorical_crossentropy", contrastive_loss],optimizer=rms, metrics=["accuracy"])


le = LabelBinarizer()
y_a = le.fit_transform(Y_train[:, 0])
y_b = le.fit_transform(Y_train[:, 1])
target = np.concatenate((y_a, y_b), -1)

model.fit([X_train[:, 0], X_train[:, 1]], y=[target, target],
          batch_size=256, epochs=50, 
          validation_split=0.2)
model.save("triplet_loss_model.h5")

model = Model(inputs=[anchor_input], outputs=[soft_anchor, pre_logits_anchor])
model.load_weights("triplet_loss_model.h5")



X_test, Y_test = generate_pair(test_data, test_target)

X_test_soft_1, X_test_embed_1 = model.predict([X_test[:,0]])
X_test_soft_2, X_test_embed_2 = model.predict([X_test[:,1]])
score=[]
test_label=[]
for i in range(len(test_target)):
    score.append(K.sqrt(K.sum(K.square(X_test_embed_1[i] - X_test_embed_2[i]))))
    if test_data[i][0]==test_target[i][1]:
        test_label.append(0)
    else:
        test_label.append(1)
print(score)

k=0.5
while k<5:
    tp,tn,fp,fn=siamese_accuracy_score(test_label,score,k)
    print(tp,tn,fp,fn)
    accuracy=(tp+tn)/(tp+tn+fp+fn)
    far=(fp)/(fp+tn)
    frr=(fn)/(fn+tp)
    print("k=",k)
    print("accuracy:",accuracy,"far:",far,"frr:",frr)
    k=k+0.1