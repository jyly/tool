# _*_ coding: utf-8 _*_
from minepy import MINE
import math
#计算多个特征的信息熵 特征集，列：不同的样本，行：不同的特征
def minecal(data,target):
	informscore=[]
	for i in range(len(data[0])):
		tempdata=[]
		for j in range(len(data)):
			tempdata.append(data[j][i])
		mine = MINE()
		mine.compute_score(tempdata, target)
		informscore.append(mine.mic())

	informsort = np.argsort(informscore)#由小到大排序
	return informsort

#根据信息熵选择特征，选择信息熵最大的前topn个特征
def mineselect(data,informsort,topn=30):
	if topn>len(data[0]):
		topn=len(data[0])
	selectdata=[]
	for i in range(len(data)):
		selectdata.append([])
		for j in range(topn):
			selectdata[i].append(data[i][informsort[-1-j]])
	return selectdata


def NMI(A,B):
	A=np.array(A)
	B=np.array(B)
	# tempa=[]
	# for i in A:
	# 	tempa.append(round(i,2))
	# A=tempa

	# tempb=[]
	# for i in B:
	# 	tempb.append(round(i,1))
	# B=tempb

	# print(A)
	# len(A) should be equal to len(B)
	total = len(A)
	A_ids = set(A)
	B_ids = set(B)
	#Mutual information
	MI = 0
	eps = 1.4e-45
	for idA in A_ids:
		for idB in B_ids:
			idAOccur = np.where(A==idA)
			idBOccur = np.where(B==idB)
			idABOccur = np.intersect1d(idAOccur,idBOccur)
			# print(idAOccur,idBOccur,idABOccur)
			px = 1.0*len(idAOccur[0])/total
			py = 1.0*len(idBOccur[0])/total
			pxy = 1.0*len(idABOccur)/total
			MI = MI + pxy*math.log(pxy/(px*py)+eps,2)
	# Normalized Mutual information
	Hx = 0
	for idA in A_ids:
		idAOccurCount = 1.0*len(np.where(A==idA)[0])
		Hx = Hx - (idAOccurCount/total)*math.log(idAOccurCount/total+eps,2)
	Hy = 0
	for idB in B_ids:
		idBOccurCount = 1.0*len(np.where(B==idB)[0])
		Hy = Hy - (idBOccurCount/total)*math.log(idBOccurCount/total+eps,2)
	# MIhat = 2.0*MI/(Hx+Hy)
	MIhat = (Hx+Hy-MI)
	print (Hx,Hy,MI,MIhat)  
	MIhat = MIhat/Hx
	print (MIhat)   
	return MIhat

import numpy as np
x = np.linspace(0, 1, 100)
y = np.sin(10 * np.pi * x) + x
# print(y)
NMI(x,y)

# mine = MINE(alpha=0.6, c=15, est="mic_approx")
mine = MINE()
mine.compute_score(x, y)
print(mine.mic())
print(metrics.normalized_mutual_info_score(x, y))

# from math import log,sqrt
# def KL_divergence(P,Q):
# 	# KL = stats.entropy(P,Q)
# 	KL=sum(_p * math.log(_p / _q) for _p, _q in zip(P, Q) if _p != 0) 
# 	# KL=np.sum([v for v in P * np.log2(P/Q) if not np.isnan(v)])
# 	return KL
# print(KL_divergence(x,x))