import os     
os.environ["PATH"] += os.pathsep + 'E:/system/python/graphviz/bin'
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





def simplemoel_mlp(input_shape):
    '''Base network to be shared (eq. to feature extraction).
    '''
    input = Input(shape=input_shape)
    x = Flatten()(input)
    #全连接层
    x = Dense(128, activation='relu')(x)
    #遗忘层
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)


    return Model(input, x)

def simplemoel_conv(input_shape):
    '''
    Base network to be shared.
    '''
    # 卷积层
    input = Input(shape=input_shape)

    x = Conv2D(16, (3, 3), activation='relu', input_shape=input_shape,padding='same')(input)
    x = Dropout(0.1)(x)

    x = Conv2D(32, (3, 3), activation='relu',padding='same')(x)
    x = Dropout(0.1)(x)

    x = Conv2D(32, (3, 3), activation='relu',padding='same')(x)
    x = Dropout(0.2)(x)

    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    return Model(input, x)

