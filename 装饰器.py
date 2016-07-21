# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 07:55:38 2016

@author: samsung
"""
import time
import random

def time_cost(f):
	def _f(*arg,**kwarg):
		start = time.clock()
		a     =f(*arg,**kwarg)
		end   = time.clock()
		print f.__name__,"run cost time is ",end-start
		return a
	return _f
@time_cost
def list_comp(length):
	return [(x,y) for x in range(length) for y in range(length) if x*y>25]
@time_cost
def for_loop(xlen,ylen):
    a=[]
    for x in range(0,xlen):
        for y in range(0,ylen):
            if x*y>25:
                a.append((x,y)) 
    return a	

def makebold(fn):
	print "makebold"
	def wrapped():
		return "<b>"+fn()+"</b>"
	return wrapped
    
def makeitalic(fn):
	print "makeitalic"
	def wrapped():
		return "<i>"+fn()+"</i>"
	return wrapped 

@makebold
@makeitalic
def hello():
	return "hello world"    
if __name__=="__main__":
	a=list_comp(1000)
	print len(a)
	b=for_loop(1000,100)
	print len(b)
	pass
	# print hello()    