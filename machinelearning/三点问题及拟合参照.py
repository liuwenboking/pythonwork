#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 
"""
有N个点，寻找到这些点的距离和最小的点。
"""

import numpy as np
from matplotlib import pyplot as plt

def fitting(A,B):
    AATN = np.linalg.inv(A.T.dot(A))
    fac = AATN.dot(A.T).dot(B)
    result = A.dot(fac)
    result = result.reshape(1,len(B))
    return result

def f(p, points):
    """
    p到points的距离和
    """
    return np.sum(np.sum((p - points) ** 2, axis=1) ** 0.5)

def fgrad(p, points):
    """
    距离和函数在p点的梯度
    """
    dx = np.sum((p[0] - points[:, 0]) / np.sum((p - points) ** 2, axis=1) ** 0.5)
    dy = np.sum((p[1] - points[:, 1]) / np.sum((p - points) ** 2, axis=1) ** 0.5)
    return np.array([dx, dy])


if __name__ == '__main__':

    # 随机或者自定义几个点，寻找距离这些点之和最小值的点。
    points = np.random.rand(5, 2)
    # points = np.array([
    #         [0,0],
    #         [2,0],
    #         [1,1.667]
    #     ])
    # x为随机初始点
    A    =np.ones([2,len(points)])
    A[0] = points.T[0]
    x1   = A[0].reshape(len(points))
    A    = A.T
    B    = points.T[1]
    
    B    = B.T
    result = fitting(A,B)
    result = result.reshape(len(points))

    x = np.random.rand(2)

    step = 0.2
    xhistory = x #用来存储历史值

    for k in range(100):
        y = f(x, points)
        xk = x - step * fgrad(x, points)
        yk = f(xk, points)
        print y,yk
        if y - yk > 1e-8:
            x = xk
            xhistory = np.vstack((xhistory, x))
        elif y - yk <0:
            #步子太大，超过极值后调整步伐大小
            step *= 0.5
        else:
            break
    print x1.shape
    plt.plot(points[:, 0], points[:, 1], 'bo')
    plt.plot(x1, result, color='g',linestyle ='-', marker ='')
    plt.plot(xhistory[:, 0], xhistory[:, 1], 'r^')
    plt.plot(xhistory[:, 0], xhistory[:, 1], 'k-')
    plt.title(u'迭代次数 = %d, 距离和 = %.3f, 极值点 = (%.3f, %.3f), 最后步长 = %f' % (k, y, x[0], x[1], step))
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.show()