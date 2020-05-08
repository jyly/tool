def pcapro(train_data,test_data,i=10):
	pca = PCA(n_components=i)
	pca = pca.fit(train_data)
	train_data=pca.transform(train_data)
	test_data=pca.transform(test_data) 
	return train_data,test_data
