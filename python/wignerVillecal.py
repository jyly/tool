from tftb.processing import WignerVilleDistribution,PseudoWignerVilleDistribution
#维格纳分布
def WignerVillecal(data):	
	dist = PseudoWignerVilleDistribution(data)
	result = dist.run()
	tfr, times, freqs=result
	x=[]
	y=[]
	z=[]
	# print(len(times))
	# print(len(freqs))
	# print(len(tfr),len(tfr[0]))
	for i in range(len(times)):
		for j in range(len(freqs)):
			x.append(times[i])#时域序号点
			y.append(freqs[j])#频域序号点
			z.append(tfr[j][i])#振频波动
	return x,y,z