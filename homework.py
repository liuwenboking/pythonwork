# -*- coding: utf-8 -*-
"""
Created on Thu Jul 07 08:28:37 2016

@author: samsung
"""

from matplotlib import pyplot as plt
import numpy as np
from math import pi,sin,cos
r = 5
def gen_circle_point(num):
    # arange类似python里的range
    t = np.arange(0, 2*pi, 2*pi/num)
    
    y = [ (sin(elem)*(r/2),cos(elem)*(r/2)) for elem in t]
    
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca()
    plt.plot(10,-10,'bo')
    plt.plot(10,10,'bo')
    plt.plot(-10,10,'bo')
    plt.plot(-10,-10,'bo')
    for center in y:        
        circle1 = plt.Circle(center, 4, color='r',fill=False)
        ax.add_artist(circle1)
        plt.plot(center[0],center[1],'bo')
          
    plt.grid(True)
    
    plt.show()

gen_circle_point(32)    


