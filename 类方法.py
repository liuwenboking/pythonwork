#!/usr/bin/env python
# coding: utf-8
# http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
class Person:
    grade=1
    def __init__(self,name):
        self.name = name
    def sayHi(self):#加self区别于普通函数
        print 'Hello, your name is?',self.name
   
    @staticmethod #声明静态，去掉则编译报错;还有静态方法不能访问类变量和实例变量
    def sayName():#使用了静态方法，则不能再使用self
        print "my name is king",#grade,self.name
    
    @classmethod #类方法
    def classMethod(cls):
    	print cls.grade #以此形式访问类属性
        print("class method") 
        
if __name__=="__main__":
	p = Person("king")
	p.sayHi()
	p.sayName()
	p.classMethod()
	Person.classMethod()
