
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

def vgg_16_base(input_tensor):
    net = Conv2D(64(3,3),activation='relu',padding='same',input_shape=(224,224,3))(input_tensor)
    net = Conv2D(64,(3,3),activation='relu',padding='same')(net)
    net = MaxPooling2D((2,2),strides=(2,2))(net)
 
    net = Conv2D(128,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(128,(3,3),activation='relu',padding='same')(net)
    net= MaxPooling2D((2,2),strides=(2,2))(net)
 
    net = Conv2D(256,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(256,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(256,(3,3),activation='relu',padding='same')(net)
    net = MaxPooling2D((2,2),strides=(2,2))(net)
 
    net = Conv2D(512,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(512,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(512,(3,3),activation='relu',padding='same')(net)
    net = MaxPooling2D((2,2),strides=(2,2))(net)
 
    net = Conv2D(512,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(512,(3,3),activation='relu',padding='same')(net)
    net = Conv2D(512,(3,3),activation='relu',padding='same')(net)
    net = MaxPooling2D((2,2),strides=(2,2))(net)
    net = Flatten()(net)
    net = Dense(128, activation='relu')(net)
    return net



