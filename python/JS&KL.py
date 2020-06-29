import numpy as np
from numpy.linalg import norm
import scipy.stats
def KL_divergence(P,Q):
	# KL=0
	# KL1=0
	# KL2=0
	# for i in range(len(P)):
	# 	KL1=KL1+P[i]*np.log(P[i]/Q[i])
	# 	KL2=KL2+Q[i]*np.log(Q[i]/P[i])
	# KL=(KL1+KL2)/2
	KL = scipy.stats.entropy(P,Q) 
	# KL=sum(_p * math.log(_p / _q) for _p, _q in zip(P, Q) if _p != 0) 
	# KL=np.sum([v for v in P * np.log2(P/Q) if not np.isnan(v)])
	return KL


def JS_divergence(p,q):
	p=np.array(p)
	q=np.array(q)
	_P = p / norm(p, ord=1)
	_Q = q / norm(q, ord=1)
	M=(_P+_Q)/2
	JS=0.5*(KL_divergence(_P,M)+KL_divergence(_Q,M))
	return JS

