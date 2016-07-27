#coding:utf-8
from bs4 import BeautifulSoup
import urllib
import re
def geturl(num):
	html = urllib.urlopen(r"http://www.heibanke.com/lesson/crawler_ex00/"+num)
	bs_obj = BeautifulSoup(html,"html.parser")
	alist = bs_obj.findAll('h3')
	for aa in alist:
		match=re.search(r"\d{1,}",aa.text)
		print aa.text
		if match:
			return aa.text[match.start():match.end()]
		else:
			return None
num=geturl("")	
while num:
	num = geturl(num)
else:
	print num	
