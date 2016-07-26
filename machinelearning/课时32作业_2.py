#coding:utf-8
#根据特征值特征向量求解斐波那契数列
#斐波那契数列可以用差分方程进行解答
#F(K+2)=F(K+1)+F(K)
#F(K+1)=F(k+1)+0
#
import numpy as np
import time
def time_cost(f):
    def _f(*arg, **kwarg):
        start = time.clock()
        a=f(*arg,**kwarg)
        end = time.clock()
        print f.__name__,"run cost time is ",end-start
        return a
    return _f



A = np.array([[1,1],[1,0]])
eigval,S=np.linalg.eig(A)
x = np.array([[1],[0]])
z=np.linalg.inv(S).dot(x)
@time_cost
def fib_eig(N):
	def lamda_n(eigval,n):
		return np.array([[eigval[0]**n,0],[0,eigval[1]**n]])
	if N>=2:
	    y=S.dot(lamda_n(eigval,N).dot(z))
	    return y[1]
	elif N<0:
	    assert False,"N must larger than zeros"
	else:
	    return x[1-N]
@time_cost	    
def fib_opt(n):
	i = 1
	b,a = 1,0
	while i<=n:
		yield b
		b,a = a+b,b
		i += 1
		

a=fib_opt(100)	    
aa=[ a.next() for i in range(100)]
opt=aa[len(aa)-1]
eig=fib_eig(100)
print opt-eig



