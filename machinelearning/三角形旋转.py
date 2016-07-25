#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
p = np.array([[1,2,3,1],[1,3,0,1]])
# 旋转角度 30
theta = np.pi / 6
#旋转矩阵
H = np.array([[np.cos(theta),-np.sin(theta)],
	          [np.sin(theta),np.cos(theta)]])
#根据绕原点旋转
pt = H.dot(p)
#绕(2
#   3 ) 向量旋转
#   
HP  = np.array([[-2,-2,-2,-2],[-3,-3,-3,-3]])
pt1 = p + HP
pt1 = H.dot(pt1)
pt1 = pt1 + HP * -1

plt.plot(p[0],p[1],'b',marker='o')
plt.plot(pt[0],pt[1],'y',marker='^')
plt.plot(pt1[0],pt1[1],'g',marker='.')


plt.xlim([-5,5])
plt.ylim([-5,5])
plt.grid(True,color='r')
plt.show()

#欧拉公式
#