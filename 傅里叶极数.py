#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np  
import matplotlib.pyplot as plt  
# from solutions_3 import *


# 产生一个方波(x,y)
x = np.linspace(-10,10,300) 
y=[]
for i in np.cos(x):
    if i>0:
        y.append(0)
    else:
        y.append(2)
y=np.array(y)


def generateA(x,n):
	m = []
	for i in range(n):
		m.append( np.cos( x*i + x))
		m.append( np.sin( x*i + x))
	return np.array(m).T

def projection(A,B):
	AATN = np.linalg.inv(A.T.dot(A))
	fac  = AATN.dot(A.T).dot(B)
	return A.dot(fac)+B.mean()

B = y.reshape(y.shape[0],1)

# write Your code, Fourier function    
plt.plot(x,y,color='g',label='origin') 
plt.plot(x,projection(generateA(x,3),B),color='r',label='3')
plt.plot(x,projection(generateA(x,8),B),color='b',label='8')
plt.plot(x,projection(generateA(x,23),B),color='k',label='23')
plt.legend()
plt.axis('equal')
plt.show()