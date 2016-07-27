#coding:utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import re
def getResult(html):
	bs_obj = BeautifulSoup(html,"html.parser")
	alist = bs_obj.findAll('h3')
	for aa in alist:
		match = re.search(u"请重新输入",aa.text)
		if match:
			return False
		else:
			return True


load = dict(username='heibanke', password='12')		
for i in range(0,31):
	load['password']=i
	r = requests.post("http://www.heibanke.com/lesson/crawler_ex01/",load)
	if getResult(r.text):
		print "{0} is success.".format(i)
		break
	else:
		print "{0} is fail.".format(i)