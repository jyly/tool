manhattan_distance = lambda x, y: np.abs(x - y)
euclidean_distance = lambda x, y: np.sqrt(np.power((x - y), 2))

#切比雪夫距离
from numpy import *
vector1 = mat([1,2,3])
vector2 = mat([4,7,5])
print abs(vector1-vector2).max()

 
#余弦夹角
cosV12 = dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))

print cosV12

# 汉明距离
matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

smstr = nonzero(matV[0]-matV[1]);

print shape(smstr[0])[1]

# 杰卡德距离
import scipy.spatial.distance as dist  # 导入scipy距离公式

matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

print ("dist.jaccard:", dist.pdist(matV,'jaccard'))