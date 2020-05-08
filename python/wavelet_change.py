# -*- coding: utf-8 -*-
import numpy as np
import pywt
import matplotlib.pyplot as plt

# 
x = np.linspace(-5, 5, 100)
y = np.sin(x)
(cA, cD) = pywt.dwt(y, 'db1')

plt.subplot(311)
plt.plot(y)

plt.subplot(312)
plt.plot(cA)

plt.subplot(313)
plt.plot(cD)

plt.show()


#小波变化，不同阶数和不同小波基的影响
from pywt import wavedec
coeffs = wavedec(y, 'haar', level=3)
cA3, cD3, cD2 , cD1= coeffs

plt.subplot(311)
plt.plot(y)

plt.subplot(312)
plt.plot(cA3)

plt.subplot(313)
plt.plot(cD3)

plt.show()