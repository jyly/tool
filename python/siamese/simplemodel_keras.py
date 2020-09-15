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
from keras.layers import Input, Flatten, Dense, Dropout, Lambda,Conv2D,MaxPooling2D
from keras.optimizers import RMSprop
from keras import backend as K
from keras import regularizers





def simplemoel(input_shape):
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


    '''
    Base network to be shared.
    '''
    # 卷积层
    # x = Conv2D(32, (7, 7), activation='relu', input_shape=input_shape, kernel_regularizer=regularizers.l2(0.01),
    #            bias_regularizer=regularizers.l1(0.01))(input)
    # x = MaxPooling2D()(x)
    # x = Conv2D(64, (3, 3), activation='relu', kernel_regularizer=regularizers.l2(0.01),
    #            bias_regularizer=regularizers.l1(0.01))(x)
    # x = Flatten()(x)
    # x = Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01),
    #           bias_regularizer=regularizers.l1(0.01))(x)


    return Model(input, x)

