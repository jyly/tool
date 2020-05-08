# -*- coding=utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt



def indexpicshow(data):
	plt.plot(range(len(data)), data, 'blue')
	plt.show()

def indexpicsave(data,savefile):
	fig = plt.figure()
	plt.plot(range(len(data)), data, 'blue')
	fig.savefig(savefile)
	plt.close()

def picshow(x,y):
	plt.plot(x, y, 'blue')
	plt.show()	

def picsave(x，y,savefile):
	fig = plt.figure()
	plt.plot(x, y, 'blue')
	fig.savefig(savefile)
	plt.close()
