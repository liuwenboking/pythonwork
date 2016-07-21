# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:55:46 2016

@author: liuwenbo_wenbo
"""

from matplotlib import pyplot as plt
import numpy as np

X=np.array([[1,2,5,7]])
Y=np.array([[1,1,3,4]])
A=np.array([[1,1],[2,1],[5,1],[7,1]])
B=np.array([[1],[1],[3],[4]])


AATN = np.linalg.inv(A.T.dot(A))

fac = AATN.dot(A.T).dot(B)

result = A.dot(fac)
    
for i in range(4):
    plt.plot(X[0][i],Y[0][i],marker='o')
result = result.reshape(1,4)
print result
plt.plot(X[0],result[0],'r',marker='^') 
plt.xlim([0,10])
plt.ylim([0,10])
plt.show()