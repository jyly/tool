# _*_ coding: utf-8 _*_

import numpy as np

# 原始数据，1m的采样频率
def fft(data, sampling_rate, fft_size=None):  
    if fft_size is None:  
        fft_size = len(data)  
    data = data[:fft_size]  
    datafft = abs(np.fft.rfft(data)/fft_size)  
    freqs = np.linspace(0, int(1.0*sampling_rate/2), int(1.0*fft_size/2+1))    #linspace(0,100,501)
    return freqs, datafft    #频域，对应振幅