# _*_ coding: utf-8 _*_

# from sklearn import tree
# X = [[0,0,0],[0,1,0],[1, 0,0],[1,0,1],[1,1,0]]
# Y = [1,2,3,4,5]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, Y)
 
# x1=clf.predict([[0, 0.,0],[0,0,1]])
# x2=clf.predict_proba([[0, 0.,0]])  
# print x1,x2


# import pydotplus 
# import os     
# os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# dot_data = tree.export_graphviz(clf, out_file=None) 
# graph = pydotplus.graph_from_dot_data(dot_data) 
# graph.write_pdf("iris.pdf")



print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict,cross_val_score,train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Parameters
n_classes = 3
plot_colors = "ryb"
plot_step = 0.2

# Load data
iris = load_iris()

# print iris

# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=1)
# print X_train
# print '\n'
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=2)
# print X_train




for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                [1, 2], [1, 3], [2, 3]]):
    # We only take the two corresponding features
    X = iris.data[:, pair]    
    # 选用不同的特征
    # if pair==[0,2]:
    #     print X
    y = iris.target
    # Train
    clf = DecisionTreeClassifier().fit(X, y)
    # 构建不同的决策树
    # Plot the decision boundary
    plt.subplot(2, 3, pairidx + 1)
    # print  clf.score(X, y)


    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    # 在不同的元素中选取最大最小值
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))

    # 绘制底层版颜色
    plt.tight_layout(h_pad=0.5, w_pad=0.5, pad=2.5)
    # 两个行相等的矩阵列组合成一个矩阵
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu)

    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])
    # 绘制点
    # Plot the training points
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                    cmap=plt.cm.RdYlBu, edgecolor='black', s=15)

plt.suptitle("Decision surface of a decision tree using paired features")
plt.legend(loc='lower right', borderpad=0, handletextpad=0)
plt.axis("tight")
plt.show()