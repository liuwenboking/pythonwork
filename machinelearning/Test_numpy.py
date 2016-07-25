#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt

x = [1,4,3,1]
y = [1,2,7,1]
plt.plot(x,y,'r',marker='o')
plt.grid(True,color='r')
plt.xlim([0,10])
plt.ylim([0,10])
plt.show()
a = np.arange(1,5)
print a
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print a,a.shape,a.size,a.ndim
b=a.flatten()
print b
c=np.eye(3)
print c
d = np.array([[3],[2],[1]])
e = np.array([3,2,1])
print e
print c.dot(e)