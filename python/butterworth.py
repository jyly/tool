# _*_ coding: utf-8 _*_
from scipy import signal

def highpass(data,high,fre,order=3):#只保留高于high频率的信号，fre是采样频率,order是滤波器阶数
	wh=high/(fre/2)
	b, a = signal.butter(order, wh, 'high')
	data = signal.filtfilt(b, a, data)
	return data

def lowpass(data,low,fre,order=3):#只保留低于low频率的信号，fre是采样频率,order是滤波器阶数
	wl=high/(fre/2)
	b, a = signal.butter(order, wl, 'low')
	data = signal.filtfilt(b, a, data)
	return data

def bandpass(data,data,start,end,fre,order=3):#只保留start到end之间的频率的信号，fre是采样频率,order是滤波器阶数
	ws = start / (fre / 2) 
	we = end / (fre / 2) 
	b, a = signal.butter(order, [ws,we], 'bandpass')
	data = signal.filtfilt(b, a, data)
	return data
