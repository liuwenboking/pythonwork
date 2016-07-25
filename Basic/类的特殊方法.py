#coding:utf-8
class Point(object):
	__slots__=["_x","_y"]
	def __init__(self,x,y):
		assert isinstance(x,int) or isinstance(x,float)
		assert isinstance(y,int) or isinstance(y,float)
		self._x = float(x)
		self._y = float(y)
	def __add__(self,other):
		assert isinstance(other,Point)
		return Point(self._x+other._x,self._y+other._y)
	def __sub__(self,other):
		assert isinstance(other,Point)
		return Point(self._x-other._x,self._y-other._y)
	def __mul__(self,p):
		assert isinstance(p,int) or isinstance(p,float)
		return Point(self._x*p,self._y*p)
	def __div__(self,p):
		assert (isinstance(p,int) or isinstance(p,float)) and p!=0
		return Point(self._x/p,self._y/p)
	def __str__(self):
		return "x is {x},y is {y}".format(x=self._x,y=self._y)
	@property
	def xy(self):
		return (self._x,self._y)

	def __repr__(self):
		return str(self.xy)

	

if __name__ =="__main__":
	point = Point(1,2)
	other = Point(2.5,3.3)
	print other - point
	print point / 2
	print point.xy
	point 
	other