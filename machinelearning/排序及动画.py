# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 08:50:27 2016

@author: samsung
"""
# get_ipython().magic(u'matplotlib qt4')
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.animation as animation
line_list = []
num = np.random.rand(50)
num =[elem * 10 for elem in num]
fig = plt.figure()  
ax  = plt.axes(xlim=(0, len(num)+1), ylim=(0, 10))



def update(frame):
    num_sorted = quickSort(num,0,len(num) -1,frame)
#    num_sorted = next(num_sort)
    for i,line in enumerate(line_list):
       line.set_data([i,i], [num_sorted[i],0])
    
def init(): 
    for i in range(len(num)):
       line,=ax.plot([i+1,i+1], [num[i],0],marker='o')  
       line_list.append(line)

def bubbleSort():
    for i in range(len(num) -1 ):
        for j in range(len(num) -1):
            if num[j]>num[j+1]:
                temp = num[j]
                num[j]=num[j+1]
                num[j+1]=temp
                yield num
                
def quickSort(num,low,high,frames):
    i=low
    j=high
    frames -= 1
    if frames < -1:
        return num
    if i>=j:
        return num
    key = num[i]   
    pos = j
    while i < j:
        if key <= num[j]:            
            num[pos],num[j]=num[j],num[pos]
            pos = pos - 1
        j = j - 1
    num[i],num[pos] = num[pos],key
    quickSort(num,low,pos -1,frames)
    quickSort(num,pos +1,high,frames)
    return num

  
num_sort = bubbleSort()
#
anim = animation.FuncAnimation(fig, update, init_func=init,
                               frames=len(num)**2, interval=50, blit=False)
plt.grid() 
plt.show()          