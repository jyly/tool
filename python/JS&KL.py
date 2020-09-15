import numpy as np
import scipy.stats
def KL_divergence(P,Q):
	# KL = scipy.stats.entropy(P,Q) 
	KL=sum(_p * math.log(_p / _q) for _p, _q in zip(P, Q) if _p != 0) 
	# KL=np.sum([v for v in P * np.log2(P/Q) if not np.isnan(v)])
	return KL


def JS_divergence(p,q):
	p=np.array(p)
	q=np.array(q)
	p_norm=0;
	q_norm=0;
	for i in p:
		p_norm=p_norm+i
	for i in q:
		q_norm=q_norm+i
	_P = p / p_norm
	_Q = q / q_norm
	M=(_P+_Q)/2
	JS=0.5*(KL_divergence(_P,M)+KL_divergence(_Q,M))
	return JS

