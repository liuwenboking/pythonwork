# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 15:43:21 2016

@author: samsung
"""

from matplotlib import pyplot as plt

x = [1,2,3,1]
y = [1,3,0,1]

plt.plot(x,y)

plt.title('Triangle')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.xticks([1,6])
plt.yticks([1,6])
plt.xticks([1,6],['a','b'])
plt.ylim([-1,4])
plt.xlim([-1,4])

plt.grid(True,color='r')

plt.show()