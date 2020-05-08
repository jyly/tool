# _*_ coding: utf-8 _*_
import numpy as np 
import matplotlib.pyplot as plt
import kalfilter
import s_gfilter

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

'''
X = np.arange(0, 5, .005) 
y = np.sin(2 * np.pi * 1 * X) 


plt.scatter(X, y, s=20, edgecolor="black",c="darkorange", label="data")
plt.plot(X, y,'b')
t=[]
for i in y:
    t.append(i)
Y=s_gfilter.savgol(t, 9, 2)
plt.plot(X, Y,'r')
plt.show()
'''

plt.scatter(X, y, s=20, edgecolor="black",c="darkorange", label="data")
plt.plot(X, y,'b')
t=[]
for i in y:
    t.append(i)
Y=kalfilter.kalfilt(t[0], t, len(t))
plt.plot(X, Y,'r')
plt.show()