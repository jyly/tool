# -*- coding=utf-8 -*-
import numpy as np

#自相关性
def get_auto_corr(timeSeries,k):
	'''
	Descr:输入：时间序列timeSeries，滞后阶数k
			输出：时间序列timeSeries的k阶自相关系数
		l：序列timeSeries的长度
		timeSeries1，timeSeries2:拆分序列1，拆分序列2
		timeSeries_mean:序列timeSeries的均值
		timeSeries_var:序列timeSeries的每一项减去均值的平方的和
	 
	'''
	l = len(timeSeries)
	#取出要计算的两个数组
	timeSeries1 = timeSeries[0:l-k]
	timeSeries2 = timeSeries[k:]
	timeSeries_mean = np.mean(timeSeries)

	timeSeries_var = np.array([i**2 for i in timeSeries-timeSeries_mean]).sum()
	auto_corr = 0
	for i in range(l-k):
		temp = (timeSeries1[i]-timeSeries_mean)*(timeSeries2[i]-timeSeries_mean)/timeSeries_var
		auto_corr = auto_corr + temp 
	return auto_corr

#相关系数
def calc_corr(a, b):
	a_avg = sum(a)/len(a)	
	b_avg = sum(b)/len(b) 	
	# 计算分子，协方差————按照协方差公式，本来要除以n的，由于在相关系数中上下同时约去了n，于是可以不除以n	
	cov_ab = sum([(x - a_avg)*(y - b_avg) for x,y in zip(a, b)]) 	
	# 计算分母，方差乘积————方差本来也要除以n，在相关系数中上下同时约去了n，于是可以不除以n
	sq = math.sqrt(sum([(x - a_avg)**2 for x in a])*sum([(x - b_avg)**2 for x in b])) 	
	corr_factor = cov_ab/sq 	
	return corr_factor

from statsmodels.tsa.stattools import acf
data=[0,1,2,1,0,-1,-2,-1,0,1,2,1,0,-1,-2,-1,0,1,2,1,0,-1,-2,-1,0,1,2,1,0,-1,-2,-1,0,1,2,1,0,-1,-2,-1,0]


result=acf(data)
print(len(result))
print(result)

result=get_auto_corr(data,1)
print(result)