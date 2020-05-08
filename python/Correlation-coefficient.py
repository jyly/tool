import math
import numpy as np
#计算a和b的相关系数
def calc_corr(a, b):
	a_avg = sum(a)/len(a)	
	b_avg = sum(b)/len(b) 	
	# 计算分子，协方差————按照协方差公式，本来要除以n的，由于在相关系数中上下同时约去了n，于是可以不除以n	
	cov_ab = sum([(x - a_avg)*(y - b_avg) for x,y in zip(a, b)]) 	
	# 计算分母，方差乘积————方差本来也要除以n，在相关系数中上下同时约去了n，于是可以不除以n
	sq = math.sqrt(sum([(x - a_avg)**2 for x in a])*sum([(x - b_avg)**2 for x in b])) 	
	corr_factor = cov_ab/sq 	
	return corr_factor


s1 = [1, 2, 3, 4, 5, 5, 5, 4]
s2 = [1, 2, 3, 4, 5, 5,4,6]

print(calc_corr(s1,s2))
#要求a和b的长度一致
print(np.corrcoef(s1,s2))