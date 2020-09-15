import matplotlib.pyplot as plt

plt.rc('font',family='Times New Roman') 

def indexpicshow(data):
	plt.plot(range(len(data)), data, 'blue')
	plt.ylabel('') 
	plt.xlabel('')
	plt.axhline()#纵
	plt.axvline()#横
	plt.show()

def pointpicshow(data):
	for i in range(len(data)):
		plt.plot(i, data[i], 'o')
	plt.show()

def mixindexpicshow(data1,data2):
	plt.subplot(311)
	plt.plot(range(len(data1)), data1, 'red')
	plt.subplot(312)
	plt.plot(range(len(data2)), data2, 'blue')
	plt.subplot(313)
	plt.plot(range(len(data1)), data1, 'red')
	plt.plot(range(len(data2)), data2, 'blue')
	plt.show()

def picshow(datax,datay):
	plt.plot(datax, datay, 'blue')
	plt.show()	

def mixmulpicshow(data1,data2,data3):
	plt.subplot(311)
	plt.plot(data3, data1, 'red')
	plt.subplot(312)
	plt.plot(data3, data2, 'blue')
	plt.subplot(313)
	plt.plot(data3, data1, 'red')
	plt.plot(data3, data2, 'blue')
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
