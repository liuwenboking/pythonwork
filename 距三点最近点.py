# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:55:46 2016

@author: liuwenbo_wenbo
"""

from matplotlib import pyplot as plt
import numpy as np

X=np.array([[1,3,2]])
Y=np.array([[3,1,6]])
A=np.array([[1,1],[3,1],[2,1]])
B=np.array([[3],[1],[6]])


AATN = np.linalg.inv(A.T.dot(A))

fac = AATN.dot(A.T).dot(B)
result = A.dot(fac)
result = result.reshape(1,3)
for i in range(3):
    plt.plot(X[0][i] ,Y[0][i]  ,marker='o')    
for i in range(3):
    plt.plot(X[0][i] -X[0][0],Y[0][i]-result[0][0]  ,marker='o')

plt.plot(X[0] -X[0][0],result[0]-result[0][0] ,'r',marker='^') 

plt.plot(X[0] ,result[0] ,'r',marker='^') 
plt.xlim([-2,7])
plt.ylim([-7,7])
plt.grid(True,color='r')
plt.show()