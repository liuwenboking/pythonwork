#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


def projection(A,B):
	AATN = np.linalg.inv(A.T.dot(A))
	fac  = AATN.dot(A.T).dot(B)
	return A.dot(fac)

if __name__ == "__main__":
	# A = np.matrix([[4.0,2.0],[1.0,3.0]])
	# B = np.matrix([[3.0],[2.0]])
	A = np.array([[1],[2],[3]])
	B = np.array([[1],[1],[1]])
	P = projection(A,B)
	print P
	x = np.linspace(-0.5,1,10)

	x.shape = (1,10)
	xx = A.dot(x)
	fig = plt.figure()
	ax = fig.gca(projection ='3d')
	ax.plot(xx[0,:],xx[1,:],xx[2,:],label='LineA')
	ax.plot([0,B[0]],[0,B[1]],[0,B[2]],label='LineB')
	ax.plot([B[0][0],P[0][0]],[B[1][0],P[1][0]],[B[2][0],P[2][0]],label='LineC',marker='o')
	# ax.plot(P[0][0],P[1][0],P[2][0],'r',marker='o')
	ax.legend()
	ax.axis("equal")
	plt.show()