# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 19:55:46 2016

"""

from matplotlib import pyplot as plt
import numpy as np

#拟合
def fitting(A,B):
	AATN = np.linalg.inv(A.T.dot(A))
	fac = AATN.dot(A.T).dot(B)
	result = A.dot(fac)
	result = result.reshape(1,len(B))
	return result

def drawPoints(X,Y):
	for i in range(len(X)):
		plt.plot(X[i],Y[i]  ,marker='o')

def drawLine(X,Y):
	plt.plot(X,Y,'r',marker='^') 

def initFig():
	plt.grid(True,color='r')
	plt.xlim([-2,7])
	plt.ylim([-2,7])
	# plt.axis("equal")

def getLefRightSumByPos(d,pos):
	leftSum = 0
	rightSum = 0
	posNum = d[pos][0]
	for i in range(pos):
		leftSum += abs(posNum - d[i][0])

	for i in range(pos,len(d)):
		rightSum += abs(posNum - d[i][0])

	return (leftSum,rightSum)

def getMinDistancePoint(d,pos):
	posNum = d[pos][0]
	leftSum = 0
	rightSum = 0
	preDiff = None
	prePos = pos
	leftSum,rightSum = getLefRightSumByPos(d, pos)
	diff = abs(leftSum - rightSum)
	
	while (diff < preDiff and pos >=0 and pos <len(d) ):
		print "diff,pos,prepos,prediff,lefsum,rightsum", diff,pos,prePos,preDiff,leftSum,rightSum
		preDiff = diff
		prePos = pos
		if leftSum > rightSum:
			pos -= 1
			leftSum,rightSum=getLefRightSumByPos(d, pos)
		else:
			pos += 1
			leftSum,rightSum=getLefRightSumByPos(d, pos)
		diff = abs(leftSum - rightSum)

	else:
		return prePos



if __name__ =="__main__":
	# 定义多多边形
	X=np.array([1,2,3,4,5]).reshape(1,5)
	Y=np.array([3,5,3,5,4]).reshape(1,5)
	# 定义A
	A=np.array([[1,1],[2,1],[3,1],[4,1],[5,1]])
	# 定义B
	B=np.array([[3],[5],[3],[5],[4]])
	# 拟合后的结果
	result = fitting(A,B)
	drawPoints(X[0], Y[0])
	# drawPoints(X[0] -X[0][0], Y[0]-result[0][0])
	drawLine(X[0],result[0])
	# drawLine(X[0] -X[0][0], result[0]-result[0][0])

	#计算各点在拟合线上的投影点
	d=[]
	for i in range(len(X[0])):
		Bi=np.array([X[0][i] - X[0][0],Y[0][i] -result[0][0]] ).reshape(2,1)
		Ai=np.array([X[0][1] - X[0][0],result[0][1]-result[0][0]]).reshape(2,1)
		P=fitting(Ai,Bi)
		d.append([P[0][0],P[0][1]])
		# drawPoints([P[0][0]], [P[0][1]])

	d.sort()
	# 获得距离各点最近的点，目前对于四边形如果投影点重合一半会有问题
	pointPos = getMinDistancePoint(d, len(d) /2 )
	drawPoints([d[pointPos][0]+X[0][0]],[d[pointPos][1]+result[0][0]])
	plt.text(d[pointPos][0]+X[0][0], d[pointPos][1]+result[0][0], 'CenterPoint')
	# 只考虑一维就可以
	initFig()

	plt.show()