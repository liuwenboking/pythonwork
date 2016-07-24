#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt 
import matplotlib.animation as animation
A = np.array([[6,1],[7,4]])/4.0
w = np.linspace(0,2*np.pi,100)
xw = np.array([np.cos(w),np.sin(w)]) 
lambdaX = A.dot(xw)

def update(num):
	s1.set_data(xw[:,0:num])
	s2.set_data(lambdaX[:,0:num])
	return s1,s2

fig = plt.figure()
s1, = plt.plot([],[],linestyle='-')
s2, = plt.plot([],[],linestyle='-')



lina=animation.FuncAnimation(fig,update,frames=100, interval=50, repeat=False)
# plt.plot(xw[0],xw[1],linestyle='-')
# plt.plot(lambdaX[0],lambdaX[1],linestyle='-')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid(True,color='r')
plt.show()