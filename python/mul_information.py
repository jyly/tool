# _*_ coding: utf-8 _*_
from minepy import MINE


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
	print Hx,Hy,MI,MIhat   
	MIhat = MIhat/Hy
	print MIhat   
	return MIhat