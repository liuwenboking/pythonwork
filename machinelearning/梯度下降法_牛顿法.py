#coding:utf-8
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def fitting(A,B):
	AATN = np.linalg.inv(A.T.dot(A))
	fac = AATN.dot(A.T).dot(B)
	result = A.dot(fac)
	result = result.reshape(1,len(B))
	return result

X = np.linspace(-5, 10, 100)
Y = 30 - 2 * X


A = np.matrix([[-2,30],[-0.5,15]])
B = np.matrix([[10],[10]])

R=A.T.dot(A)
P=A.T.dot(B)


w=np.matrix([[0],[2]])
w_n=np.matrix([[10],[2]])
for i in range(100):
    w_t = w[:,-1]
    w=np.hstack((w,w_t-0.5*(R.dot(w_t)-P)))

H=np.matrix([[2*R[0,0],R[0,1]+R[1,0]],[R[0,1]+R[1,0],2*R[1,1]]])

for i in range(30):
	w_t= w_n[:,-1]
	w_n=np.hstack((w_n,w_t-H.I.dot(R.dot(w_t)-P)))

print w_n,w