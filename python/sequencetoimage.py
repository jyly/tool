import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2 as cv
from pyts.image import RecurrencePlot,MarkovTransitionField,GramianAngularField
'''
读取时间序列的数据
怎么读取需要你自己写
'''
#把数据转成array形式

sampling_rate=200
t=np.arange(0, 3, 1.0/sampling_rate)
# x1=np.sin(2*np.pi*t)
x1=np.sin(2*np.pi*t)
print(len(t))
plt.plot(t,x1)
plt.show()

TSC=x1
TSC = np.array(TSC)


# result = TSC.reshape((30, 20))
# pilresult = (result - np.min(result)) / (np.max(result) - np.min(result))
# print(pilresult)
# im = Image.fromarray(pilresult*255.0)
# im.convert('L').show()
# im.convert('L').save("PIL.jpg",format = 'jpeg')

#opencv
# cv.imshow('GrayImage', result)
# # print image's array
# cv.waitKey()


# rpresult=[[i,TSC[i]] for i in range(len(TSC))]



#Recurrence Plot
rpresult=[]
rpresult.append(TSC)
rpresult.append(TSC)
rpresult=np.array(rpresult)
print(rpresult.shape)

rp = RecurrencePlot(threshold='point', percentage=20)
X_rp = rp.fit_transform(rpresult)
X_rp=np.array(X_rp)
print(X_rp.shape)
plt.figure(figsize=(5, 5))
plt.imshow(X_rp[0], cmap='binary', origin='lower')
plt.title('Recurrence Plot', fontsize=16)
plt.tight_layout()
plt.show()


# MTF transformation

# MTFresult=[]
# MTFresult.append(TSC)
# MTFresult=np.array(MTFresult)
# print(MTFresult.shape)
# mtf = MarkovTransitionField(image_size=24)
# X_mtf = mtf.fit_transform(MTFresult)
# print(X_mtf.shape)
# print(X_mtf[0])
# # Show the image for the first time series
# plt.figure(figsize=(5, 5))
# plt.imshow(X_mtf[0], cmap='rainbow', origin='lower')
# plt.title('Markov Transition Field', fontsize=18)
# plt.colorbar(fraction=0.0457, pad=0.04)
# plt.tight_layout()
# plt.show()

# Transform the time series into Gramian Angular Fields

Gresult=[]
Gresult.append(TSC)
Gresult.append(TSC)
Gresult=np.array(Gresult)
gasf = GramianAngularField(image_size=28, method='summation')
X_gasf = gasf.fit_transform(Gresult)
gadf = GramianAngularField(image_size=28, method='difference')
X_gadf = gadf.fit_transform(Gresult)

X_gasf=np.array(X_gasf)
X_gadf=np.array(X_gadf)
print(X_gasf.shape)
print(X_gadf.shape)
# Show the results for the first time series
axs = plt.subplots()
plt.subplot(211)
plt.imshow(X_gasf[0], cmap='rainbow', origin='lower')
plt.title("GASF", fontsize=16)
plt.subplot(212)
plt.imshow(X_gadf[0], cmap='rainbow', origin='lower')
plt.title("GADF", fontsize=16)

#plt.axes((left, bottom, width, height)
cax = plt.axes([0.7, 0.1, 0.02, 0.8])
plt.colorbar(cax = cax)
plt.suptitle('Gramian Angular Fields', y=0.98, fontsize=16)
plt.tight_layout()
plt.show()