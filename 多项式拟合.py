#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np  
import matplotlib.pyplot as plt  
    
x = np.arange(-1,1,0.02)  
y = ((x*x-1)**3+1)*(np.cos(x*2)+0.6*np.sin(x*1.3))

y1 = y+(np.random.rand(len(x))-0.5)






##################################
### write your code to gen A,b

m = []
for i in range(7):
	m.append(x ** i)
A = np.array(m).T

##################################

def projection(A,b):
    ####
    # return A*inv(AT*A)*AT*b
    ####
    AA = A.T.dot(A)
    w=np.linalg.inv(AA).dot(A.T).dot(b)
    return A.dot(w)

result = projection(A,y1)
#yw = projection(A,b)
#yw.shape = (yw.shape[0],)

plt.plot(x,y,color='g',linestyle='-',marker='') 
plt.plot(x,y1,color='m',linestyle='',marker='o')
plt.plot(x,result,color='r',linestyle='-',marker='.')

plt.show()
