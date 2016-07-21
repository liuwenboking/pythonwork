# coding:utf-8
import math

class TestClass(object):
	TestAttr = u"测试的".encode("utf-8")
	"""this is a class TestClass"""
	__slots__=('width','length','x','y')
	def getName(self):
		return TestClass.__name__
	def __init__(self,width,length):
		self.width  = width
		self.length = length

if __name__=="__main__":
	f = TestClass(width=20,length=100)
	print f.width
	print TestClass.TestAttr
	f.x = 1
	print f.x
	print f.getName()
	print "hello,World"