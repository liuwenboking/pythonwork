# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 08:28:37 2016

@author: samsung
"""

from matplotlib import pyplot as plt
import numpy as np

# arange类似python里的range
t = np.arange(0, 5, 0.2)

fig = plt.figure(figsize=(10,6))

#行, 列, 序号
ax1 = fig.add_subplot(321) 
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(312)
ax4 = fig.add_subplot(325) 
ax5 = fig.add_subplot(326)

ax1.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax1.grid(True)
ax1.set_title('plot')

ax2.semilogy(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax2.grid(True)
ax2.set_title('ylog')

ax3.loglog(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax3.grid(True)
ax3.set_title('loglog')

ax4.loglog(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax4.grid(True)
ax4.set_title('loglog')

ax5.semilogy(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
ax5.grid(True)
ax5.set_title('ylog')

fig.suptitle('normal vs ylog vs loglog')
fig.subplots_adjust(hspace=0.4)

plt.show()