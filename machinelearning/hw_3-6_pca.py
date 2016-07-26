#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke

import numpy as np
import matplotlib.pyplot as plt  
from load_MNIST import *


trainX,trainy,testX,testy=get_data(Only0=False,N=2000)
data=trainX[:,1:]
def pca(data,k=0.9):
	dataTT      = data.T.dot(data)
	val,vects   = np.linalg.eig(dataTT)
	valSortInd  = np.argsort(val)
	valSortInd  = valSortInd[:-(int(k*len(val)) + 1):-1]
	redEigVects = vects[:, valSortInd]
	lowDDataMat = data.dot(redEigVects)      #求新的数据矩阵  
	reconMat    = (lowDDataMat.dot(redEigVects.T))   
	reduceData  = lowDDataMat 
	return reconMat
def svd(dataMat, k=0.9):  
    covMat = np.cov(dataMat, rowvar=0)   #求协方差方阵  
    u,s,v = np.linalg.svd(covMat)    
    print u
    for i in xrange(len(s)-1):
        if sum(s[:i+1])/sum(s) > k:
            print i
            break
    u_s = u[:,:i+1] 
    lowd_sample = u_s.T.dot(dataMat.T)
    recon_sample = u_s.dot(lowd_sample)              
    return recon_sample.T  

def show_pic(sample,recon_sample):
    N = sample.shape[0]
    a=np.zeros((28*N,28*2))
    for i in xrange(N):
        a[28*i:28*(i+1),:28]=sample[i,:].reshape(28,28)
        a[28*i:28*(i+1),28:]=recon_sample[i,:].reshape(28,28)
    plt.imshow(np.floor(a),cmap="gray")
    plt.show()
"""
# write Your code
# def pca(data,k=0.9):
    # data 原始的图片
    # k是保留特征值的百分比
    # return 返回降维后重建的图片

# def show_pic(origin_data, low_dim_):

# N is number of pic to show in the figure
# data 是 N*784 矩阵
# recon_data 是压缩后再重建的 N*784 矩阵
"""
N = 5
recon_data = svd(data,k=0.9)
show_pic(data[:N,:],recon_data[:N,:])

