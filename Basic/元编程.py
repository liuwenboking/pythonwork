#coding:utf-8
import inspect
import urllib
A = type("T",(object,),{"age":20,"height":172})
print inspect.getmro(A)
a = A()
print a.age,a.height