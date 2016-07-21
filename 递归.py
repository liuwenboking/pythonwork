# coding:utf-8
import time
def time_cost(timef):
	def decorator(f):
		def _f(*arg,**kwarg):
			start = timef()
			a     =f(*arg,**kwarg)
			end   = timef()
			print f.__name__," run cost time is ",end-start
			return a
		return _f
	return decorator


def fib(n):
	if n<=2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def reverse_s(s):
	if len(s)<=1:
		return s
	else:
		return reverse_s(s[1:])+s[0]

def fib_opt(n):
	a,b,i=1,1,1
	while i<n:
		a,b=b,a+b
		i+=1
	else:
		return a

def fib_iter():
	a,b=0,1
	while True:
		yield b
		a,b = b,a+b
def h():
    print 'Wen Chuan',
    m = yield 5  # Fighting!
    print m
    d = yield 12
    print 'We are together!'


@time_cost(time.clock)
def normal_fib(length):
	return [fib_opt(i) for i in range(1,length)]
@time_cost(time.clock)
def yield_fib(length):
	A      = fib_iter()
	result =[A.next() for i in xrange(length)]
	return result

if __name__=="__main__":
	# a=normal_fib(10000)
	# b=yield_fib(10000)
	# c = h()
	# m = c.next()  #m 获取了yield 5 的参数值 5
	# d = c.send('Fighting!')  #d 获取了yield 12 的参数值12
	# print 'We will never forget the date', m, '.', d
	A      = fib_iter()
	result =[A.next() for i in xrange(1000)]
	B      = fib_iter()
	result1 =[B.next() for i in xrange(10)]
	print result[99],result1[9]
