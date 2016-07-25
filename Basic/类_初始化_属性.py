#coding:utf-8
class Car(object):
	__slots__=["_length","_width","__owner"]
	def __init__(self,length,width,owner=None):
		self._length = length
		self._width = width
		self.__owner = owner
	def getLength(self):
		return self._length
	def setLength(self,length):
		assert length>0,"length must larger than 0"
		self._length = length
	def getWidth(self):
		return self._width
	def setWidth(self,width):
		assert width>0,"width must larger than 0"
		self._width = width
	def getOwner(self):
		return self.__owner
	def setOwner(self,owner):
		self.__owner = owner

class Suv(object):
	__slots__=["_length","_width","__owner"]
	def __init__(self,length,width,owner=None):
		self._length = length
		self._width = width
		self.__owner = owner
	@property
	def length(self):
		return self._length
	@length.setter
	def length(self,value):
		assert value>0,"length must larger than 0"
		self._length = value
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		assert value>0,"width must larger than 0"
		self._width = value
	@property
	def owner(self):
		return self.__owner
	@owner.setter
	def owner(self,value):
		self.__owner = value

class Csv(object):
	__slots__=["length","width","owner","__dict__"]
	def __init__(self,length,width,owner=None):
		self.length = length
		self.width = width
		self.owner = owner

	def __getattr__(self,name):
		print "__getattr__",name
		assert name in self.__slots__,"Not have this attribute ["+name+"]"
		return self.__dict__.get(name,None)

	def __setattr__(self,name,value):
		print "__setattr__",name
		assert name in self.__slots__,"Not have this attribute ["+name+"]"

		self.__dict__[name]=value


	

if __name__ == "__main__":
	a=Car(4700, 1920)
	a._length = -10
	#a.__owner会出错
	print a.getOwner()
	a.setOwner("lwb")
	print a.getOwner()
	a._Car__owner="test"
	print a.getOwner()

	b=Suv(4900, 2100)
	print b.length
	b._Suv__owner="test"
	print b.owner
	b._length = -1
	print b.length

	c= Csv(4900, 2100)
	# print c.name
	print c.length
	print c.owner
	#如果访问不存在的属性发生循环调用，最终栈溢出
	# print c.aa————
	c.length = -1
	print c.length
	
