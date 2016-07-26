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



A = np.array([[0.8,0.1],[0.2,0.9]])
eigval,S=np.linalg.eig(A)
x = np.array([[3200],[4000]])
z=np.linalg.inv(S).dot(x)
@time_cost
def fib_eig(N):
	def lamda_n(eigval,n):
		return np.array([[eigval[0]**n,0],[0,eigval[1]**n]])
	if N>=2:
	    y=S.dot(lamda_n(eigval,N).dot(z))
	    return y
	elif N<0:
	    assert False,"N must larger than zeros"
	else:
	    return x
eig=fib_eig(100)
print eig
