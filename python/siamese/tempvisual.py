import keras
import numpy as np
import matplotlib.pyplot as plt

import random

from keras.callbacks import TensorBoard
from keras.datasets import mnist
from keras.models import Model
from keras.layers import Input, Flatten, Dense, Dropout, Lambda
from keras.optimizers import RMSprop
from keras import backend as K

import os     
os.environ["PATH"] += os.pathsep + 'E:/system/python/graphviz/bin'

num_classes = 10
epochs = 20

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

print(x_train)
print(y_train)
x_train /= 255
x_test /= 255

print(x_train)
print(y_train)
print('\n')
print(x_test)
print(y_test)
print('\n')

input_shape = x_train.shape[1:]
print(len(x_train))
print(x_train.shape)
print(input_shape)

num_classes=10
digit_indices = [np.where(y_train == i)[0] for i in range(num_classes)]
print(digit_indices)


a = np.arange(27)
print(np.where(a > 5))

t=[len(digit_indices[d]) for d in range(num_classes)]
print(t)

n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
print(n)
labels = [1, 0]
for i in range(3):
	labels += [1, 0]
print(labels)

a=[[1,2],[3,4]]
x,y=a
print(x)
print(y)