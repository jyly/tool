# _*_ coding: utf-8 _*_

import numpy as np

import matplotlib.pyplot as plt

from sklearn import neighbors

 

# random the data as the training data
# 生成50随机个数据点
x = 5 * np.random.random((50, 2))
# 要求的最近点
y = np.array([[1, 3], [4, 2]])

 

# knn
# 最近的5个点
n_neighbors = 5

 

# create color maps

from matplotlib.colors import ListedColormap

cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

 

# fit the training data

from sklearn.neighbors import NearestNeighbors
# 生成模型
nbrs = NearestNeighbors(n_neighbors = n_neighbors, algorithm = 'auto');

nbrs.fit(x)

 

# get the nearest neighbors

distances, indices = nbrs.kneighbors(y)

print "distance:",distances

print "indices:",indices

 

# get the selection of nearest neighbors

selected = nbrs.kneighbors_graph(y).toarray()

print "selected:",selected

 

# plot the point

plt.plot(y[:,0], y[:,1], 'g+')

 

# plot the area

t = np.linspace(0, np.pi * 2, 50)

x_t = np.cos(t)

y_t = np.sin(t)

for i in range(y.shape[0]) :

    plt.plot(x_t * distances[i, -1] + y[i, 0], y_t * distances[i, -1] + y[i, 1])

 

#  all selected

selected = selected[0, :].astype(np.bool) | selected[1, :].astype(np.bool)

selected = selected.astype(np.int32)

 

# plot the selection

plt.scatter(x[:, 0], x[:, 1], c = selected, cmap = cmap_bold, edgecolor = 'k', s = 20)

 

plt.show()
