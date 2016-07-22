# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:45:15 2016

@author: liuwenbo_wenbo
"""
get_ipython().magic(u'matplotlib inline')
from matplotlib import pyplot as plt
import numpy as np
x = [1,2,3,1]
y = [1,3,0,1]
plt.plot(x,y,'b',marker='o',label="one")
plt.plot(np.array(x) -1,np.array(y) -1,'g',linestyle="-",marker='^',linewidth='2',label=u"二")
plt.plot(np.array(x)-2,np.array(y)*2,'k',linestyle="-.",marker='.',linewidth='2',label="Three")

plt.title("triangle")
plt.grid(True,color='r')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.legend()
plt.show()
