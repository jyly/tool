# _*_ coding: utf-8 _*_

import numpy as np

#快傅里叶变换，获取频域和对应的振幅
def fft(data, sampling_rate, fft_size=None):  
    if fft_size is None:  
        fft_size = len(data)  
    data = data[:fft_size]  
    #实数求解
    datafft = abs(np.fft.rfft(data)/fft_size*2)  
    freqs = np.linspace(0, int(1.0*sampling_rate/2), int(1.0*fft_size/2+1))    #linspace(0,100,501)
   	#实部和虚部的求解
    # datafft = abs(np.fft.fft(data)/fft_size*2)
	# freqs = np.linspace(0, int(1.0*1000/2), int(1.0*len(data)))    #linspace(0,100,501)

    # picshow(freqs,datafft)
    return freqs, datafft    #频域，对应振幅

#计算倒频谱
def ceps(data, sampling_rate, fft_size=None):  
    if fft_size is None:  
        fft_size = len(data)  
    data = data[:fft_size]  
    datafft = abs(np.fft.fft(data))  
    freqs = np.linspace(0, int(1.0*sampling_rate/2), int(1.0*fft_size))    #linspace(0,100,501)
    ceps=np.fft.ifft(np.log(np.abs(datafft))).real
    # picshow(freqs,datafft)
    return freqs[1:], np.abs(ceps[1:])    #频域，对应振幅

