# -*- coding=utf-8 -*-
import numpy as np
#根据时间戳，从新按频率重新再采样
def insertfilt(data,timestamp,fre):
	# picshow(timestamp,data)
	sample_interval=1000/fre
	filtdata=[]
	lasttime=timestamp[0]
	lastdata=data[0]
	localtime=timestamp[0]+sample_interval
	for i in range(len(timestamp)):
		if localtime==timestamp[i]:
			lastdata=data[i]
			lasttime=localtime
			localtime=localtime+sample_interval
			filtdata.append(data[i])
		else:
			if localtime<timestamp[i]:
				# print (localtime,timestamp[i],lasttime)
				k=(data[i]-lastdata)/(timestamp[i]-lasttime)
				lastdata=lastdata+k*sample_interval
				filtdata.append(lastdata)
				lasttime=localtime
				localtime=localtime+sample_interval
	return filtdata