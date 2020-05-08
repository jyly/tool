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