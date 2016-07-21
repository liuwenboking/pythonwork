# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:40:08 2016

@author: liuwenbo_wenbo
"""
get_ipython().magic(u'matplotlib inline')
from matplotlib import pyplot as plt
import numpy as np
t = np.arange(0,5,0.2)
x =[1,3,3,1]
y =[3,1,3,3]
fig = plt.figure()
ax = fig.add_subplot(131)
ax.plot(t,t,'-',t,t**2,'^',t,t**3,'.')
ax.grid(True,color='r')

ax1 = fig.add_subplot(132)
ax1.semilogy(t,t,'-',t,t**2,'^',t,t**3,'.')
ax1.grid(True,color='r')
ax2 = fig.add_subplot(133)
ax2.loglog(t,t,'-',t,t**2,'^',t,t**3,'.')
ax2.grid(True,color='r')

fig.show()