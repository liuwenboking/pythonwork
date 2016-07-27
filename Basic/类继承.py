#coding:utf-8
import inspect
class Employee(object):
	def __init__(self,name,job=None,pay=0):
		self._name = name
		self._job  = job
		self._pay  = pay
	def giveRaise(self,percent):
		self._pay = int(self._pay * (1+percent))
	def __str__(self):
		return "[Employee:%s,%s,%s]"%(self._name,self._job,self._pay)
class Manager(Employee):
	def __init__(self,name,job='Mgr',pay=0):
		Employee.__init__(self,name,job,pay)
	def giveRaise(self,percent,bonus=.10)		:
		Employee.giveRaise(self,percent + bonus)

class A:
	a=1
class B(A):
	b=2
class C(A):
	a=3
	b=3
	c=3
class D(B,C):
	pass

class AA(object):
	a=1
class BB(AA):
	b=2
class CC(AA):
	a=3
	b=3
	c=3
class DD(BB,CC):
	pass	
if __name__=="__main__":
	dd=DD()
	d=D()
	print "a={0},b={1},c={2}".format(d.a,d.b,d.c)
	print "a={0},b={1},c={2}".format(dd.a,dd.b,dd.c)
	print inspect.getmro(D)
	print inspect.getmro(DD)
	print inspect.getmro(Employee)		
	xiaoming = Employee("xiaoming",pay=4000)
	xiaozhang = Manager("xiaozhang",pay=6000)
	xiaozhang.giveRaise(0.1)
	xiaoming.giveRaise(0.1)
	print xiaoming
	print xiaozhang.__class__.__base__.__dict__
	print xiaozhang
