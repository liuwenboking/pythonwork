#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np  
import matplotlib.pyplot as plt  

#拟合
def fitting(A,B):
	AATN = np.linalg.inv(A.T.dot(A))
	fac = AATN.dot(A.T).dot(B)
	result = A.dot(fac)
	result = result.reshape(1,len(B))
	return result

def drawLine(X,Y):
	plt.plot(X,Y,'r',linestyle='',marker='.') 

x = np.arange(-1,1,0.02)

y = 2*np.sin(x*2.3)+0.5*x**3

A      = np.ones([2,100])
A[0]   = x
A      = A.T
y1     = y+0.5*(np.random.rand(len(x))-0.5)

B      = y1.reshape(len(y1),1)

result = fitting(A,B)
result = result.reshape(100)

print x.shape

plt.plot(x,y,color='g',linestyle='-',marker='') 
plt.plot(x,y1,color='m',linestyle='',marker='o')
plt.plot(x,result,color='r',linestyle='-',marker='')

# 把拟合的曲线在这里画出来

plt.show()