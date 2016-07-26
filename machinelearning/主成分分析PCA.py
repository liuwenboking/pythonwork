#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt

def pca(data,topN):
	dataAvg     = np.mean(data,axis = 0)
	meanMoved   = data - dataAvg
	dataTT      = meanMoved.T.dot(meanMoved)
	val,vects   = np.linalg.eig(dataTT)
	valSortInd  = np.argsort(val)
	valSortInd  = valSortInd[:-(topN + 1):-1]
	redEigVects = vects[:, valSortInd]
	lowDDataMat = meanMoved.dot(redEigVects)      #求新的数据矩阵  
	reconMat    = (lowDDataMat.dot(redEigVects.T)) + dataAvg  
	reduceData  = lowDDataMat + np.mean(data)

	return reduceData,reconMat  


N    = 100
x    = np.linspace(2, 4,100)
y    = x * 2 - 4

x1   = x+(np.random.rand(N)-0.5)*1.5
y1   = y+(np.random.rand(N)-0.5)*1.5
data = np.array([x1,y1])
a,b  = pca(data.T, 1)
plt.plot(x1,y1,linestyle=' ',marker='o')
plt.plot(x,y,linestyle='-')
plt.plot(b[:,0],b[:,1],color='r',linestyle='',marker='>',label='recon')
plt.plot(a[:,0],np.zeros(N),color = 'y',linestyle=' ',marker='o')


plt.show()