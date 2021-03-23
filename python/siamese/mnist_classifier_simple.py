import os     
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID" 
os.environ["CUDA_VISIBLE_DEVICES"]="-1"    
os.environ["PATH"] += os.pathsep + 'E:/system/python/graphviz/bin'
import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt

import random

from keras.callbacks import TensorBoard
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout, Lambda,Conv2D,MaxPooling2D,LeakyReLU
from keras.optimizers import RMSprop
from keras import backend as K
from keras import regularizers

#计算多分类的准确度
def mul_accuracy_result(target,result,divnum):#目标，结果，目标对象的数量
    tp=0
    tn=0
    fp=0
    fn=0

    for i in range(0,divnum):
        for j in range(len(result)):
            if np.argmax(result[j])==i:
                if target[j][0]==i:
                    tp=tp+1
                else:
                    fp=fp+1
            else:
                if target[j][0]==i:
                    fn=fn+1
                else:
                    tn=tn+1
    return tp,tn,fp,fn

def simplemoel_mlp(input_shape):
    '''Base network to be shared (eq. to feature extraction).
    '''
    input = Input(shape=input_shape)
    x = Flatten()(input)
    x = Dense(512)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dense(1024)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dense(256)(x)
    x = LeakyReLU(alpha=0.2)(x)
    x = Dense(10,activation='sigmoid')(x)

    return Model(input, x)



epochs = 20

# the data, split between train and test sets
(train_data, train_target), (test_data, test_target) = mnist.load_data()
train_data = train_data.astype('float32')
test_data = test_data.astype('float32')
train_data /= 255
test_data /= 255
input_shape = train_data.shape[1:]

print(train_target[:10])
print(input_shape)
# print(test_data[0])

input_shape = (28,28,1)
train_data=train_data.reshape(train_data.shape[0], 28, 28, 1)  
test_data=test_data.reshape(test_data.shape[0], 28, 28, 1)  
train_target=train_target.reshape(train_target.shape[0], 1)  
test_target=test_target.reshape(test_target.shape[0], 1)  
print(train_data.shape,train_target.shape)
print(test_data.shape,test_target.shape)


# 自定义层
model=simplemoel_mlp(input_shape)

model.summary()
rms = RMSprop()
model.compile(loss='sparse_categorical_crossentropy', optimizer=rms, metrics=['accuracy'])


history=model.fit(train_data, train_target,
          batch_size=4096,epochs=10,
          validation_split=0.2)



# compute final accuracy on training and test sets
y_pred = model.predict(train_data)
print(train_target)
print(y_pred)
y_pred = model.predict(test_data)
print(test_target)
print(y_pred)
print(np.argmax(y_pred[0]))

tp,tn,fp,fn=mul_accuracy_result(test_target,y_pred,10)
accuracy=(tp+tn)/(tp+tn+fp+fn)
far=(fp)/(fp+tn)
frr=(fn)/(fn+tp)
print("accuracy:",accuracy,"far:",far,"frr:",frr)
