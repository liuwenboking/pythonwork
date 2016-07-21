#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
A  = np.array([[1,3,5,6],[1,2,7,8]])
TA = np.array([[1,1],[1,3],[1,5],[1,6]])
B  = np.array([[1],[2],[7],[8]])

TAT = np.linalg.inv(TA.T.dot(TA))
fac = TAT.dot(TA.T)
fac = fac.dot(B)
print fac
print A.dot(TA.dot(fac))
# A = np.array([[1,]])


plt.plot(A[0][0],A[1][0],marker='o')
plt.plot(A[0][1],A[1][1],marker='o')
plt.plot(A[0][2],A[1][2],marker='o')
plt.plot(A[0][3],A[1][3],marker='o')
plt.xlim([-10,10])
plt.ylim([-10,10])
plt.show()