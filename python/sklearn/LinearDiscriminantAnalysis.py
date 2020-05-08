# _*_ coding: utf-8 _*_
import numpy as np
from sklearn import preprocessing

data = np.array([[-1, 4,3], [-3, -1,4], [-2, -7,2], [1, 8,6], [3, 1,2], [4, 2,2]])
y = np.array([1, 1, 1, 2, 2, 2])
clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,
              solver='svd', store_covariance=False, tol=0.0001)
print(clf.predict([[-0.8, -1]]))


def ldapro(train_data,test_data,train_target):
	lda = LinearDiscriminantAnalysis()
	lda = lda.fit(train_data, train_target)
	#转换矩阵
	scalings=lda.scalings_
	train_data=lda.transform(train_data)
	test_data=lda.transform(test_data) 	
	return train_data,test_data