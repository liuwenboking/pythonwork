from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot(111,projection='3d')

z = np.linspace(0, 5, 1000)
r = 1*z
x = r * np.sin(np.pi*2*z)
y = r * np.cos(np.pi*2*z)

ax.plot(x, y, z, label=u'螺旋线', c='r')
ax.legend()

# dpi每英寸长度的点数
plt.savefig('3d_fig.png',dpi=200)
plt.show()