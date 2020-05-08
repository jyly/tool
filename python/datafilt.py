# -*- coding=utf-8 -*-
import numpy
from sklearn.preprocessing import MinMaxScaler,StandardScaler

#标准化
def std(data):
    filtdata=[]
	data=np.array(data).reshape(-1,1)
	minMax = MinMaxScaler()
	data= minMax.fit_transform(data)
	for knum in data:
		filtdata.append(knum[0])
	return filtdata

#0-1化
def minmax(data):
	filtdata=[]
    data=np.array(data).reshape(-1,1)
    stdard = StandardScaler()
    data= stdard.fit_transform(data)
    for knum in data:
        filtdata.append(knum[0])
    return filtdata


#中值滤波
def meanfilt(datalist,interval,adddis=1):
	filtlist=[]
	for i in range(0,len(datalist)-interval,adddis):
		filtlist.append(np.mean(datalist[i:i+interval]))
	return filtlist

#卡尔曼滤波	
def kalman(ymean,y,winsize):	#开头，线段，窗口
	sz = (winsize,)
	xhat=numpy.zeros(sz)	  # a posteri estimate of x
	P=numpy.zeros(sz)		 # a posteri error estimate
	xhatminus=numpy.zeros(sz) # a priori estimate of x
	Pminus=numpy.zeros(sz)	# a priori error estimate
	K=numpy.zeros(sz)		 # gain or blending factor
	R = 1 # estimate of measuremet variance, change to see effect
	Q = 0.1 # process variance
	# intial guesses
	xhat[0] = ymean
	P[0] = 1.0
	for k in range(1,winsize):
		# time update
		xhatminus[k] = xhat[k-1]  #X(k|k-1) = AX(k-1|k-1) + BU(k) + W(k),A=1,BU(k) = 0
		Pminus[k] = P[k-1]+Q	  #P(k|k-1) = AP(k-1|k-1)A' + Q(k) ,A=1
		# measurement update
		K[k] = Pminus[k]/( Pminus[k]+R ) #Kg(k)=P(k|k-1)H'/[HP(k|k-1)H' + R],H=1
		xhat[k] = xhatminus[k]+K[k]*(y[k]-xhatminus[k]) #X(k|k) = X(k|k-1) + Kg(k)[Z(k) - HX(k|k-1)], H=1
		P[k] = (1-K[k])*Pminus[k] #P(k|k) = (1 - Kg(k)H)P(k|k-1), H=1
	return xhat

"""
 * Savitzky-Golay平滑滤波函数
 * data - list格式的1×n纬数据
 * window_size - 拟合的窗口大小	窗口越大越平滑
 * rank - 拟合多项式阶次 阶次越高，越贴和原来图像
 * ndata - 修正后的值
"""
def savgol(data, window_size, rank):
	size = int((window_size - 1) / 2)
	odata = data[:]
	# 处理边缘数据，首尾增加size个首尾项
	for i in range(size):
		odata.insert(0,odata[0])
		odata.insert(len(odata),odata[len(odata)-1])
	# 创建X矩阵
	x = []
	for i in range(2 * size + 1):
		m = i - size
		row = [m**j for j in range(rank)]
		x.append(row) 
	x = np.mat(x)

	# 计算加权系数矩阵B
	b = (x * (x.T * x).I) * x.T
	a0 = b[size]
	a0 = a0.T
	# 计算平滑修正后的值
	ndata = []
	for i in range(len(data)):
		y = [odata[i + j] for j in range(window_size)]
		y1 = np.mat(y) * a0
		y1 = float(y1)
		ndata.append(y1)
	return ndata

