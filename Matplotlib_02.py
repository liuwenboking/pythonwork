# -*- coding: utf-8 -*-
"""
Created on Wed Jul 06 15:49:06 2016

@author: samsung
"""

from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,1]
y = [1,3,0,1]

# np.array将列表转换成numpy的数组后可以支持广播broadcast运算
plt.plot(x,y,color='r',linewidth='2',linestyle='--',marker='D', label='one')
plt.plot(np.array(x)+1,np.array(y)+1,color='g',linewidth='3',linestyle=':',marker='o', label='two')
plt.plot(np.array(x)+2,np.array(y)+3,color='k',linewidth='1',linestyle='-.',marker='>', label='three')

plt.grid(True)
plt.legend()
plt.legend(loc='upper left')

plt.show()