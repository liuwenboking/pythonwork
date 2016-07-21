# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 08:38:29 2016

@author: samsung
"""

x=9
def f1():
    global x
    print x
    x=8
    def f2():
        print "in f2()",x
    f2()
    print "in f1()",x

def testArgs(a,b=2,c=3):
    print a,b,c

def testMoreArgs(a,*args,**kwargs):
    print a,args,kwargs

"""

"""
def sqrt(num):
    """
    自己实现的SQRT方法
    """
    assert num>=0
    high =max(num,1)
    low = 0
    
    tmp = (high + low) * 1.0 / 2.0
    
    while ( abs(tmp * tmp - num)) >0.0001:
        if tmp * tmp > num:
            high = tmp
        else:
            low  = tmp
        tmp = (high + low) * 1.0 / 2.0
    return tmp
    
def ft(f,a,b) :
    print f(a,b)

def inc(x):
    return x+10
def abc(a,b,c):
    return a*10000+b*100+c
    
  
if __name__=="__main__":
    f1()
    testArgs(1,b=10,c=100)
    testMoreArgs(1,2,3,4,5,c=2,d=3,e=4)
    ft(lambda x,y: x-y,2,3)
    a=[1,2,3]
    b=[4,5,6]
    c=[7,8,9]
    print map(abc,a,b,c)
    print map(inc,a)
    print reduce(lambda x,y:x+y,map(inc,map(abc,a,b,c)))
    print sqrt(0.25)
    print sqrt.__doc__