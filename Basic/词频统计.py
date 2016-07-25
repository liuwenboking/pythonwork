# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:59:03 2016

@author: samsung
"""
import re
word_freq_list = {}
def filterWord(word):
    filterList = ["of","and","is","to","by","a","an","the"]
    if re.match("\w+",word):
        word = re.match("\w+",word).group().lower()
        if not word in filterList:
            if word_freq_list.has_key(word):
                word_freq_list[word] += 1
            else:
                word_freq_list[word] = 1

def readFile(filename):
    f = open(filename,'r');
    try:
        line=f.readline()
        while line:
            map(filterWord,line.split(" "))
            line=f.readline()
    finally:
        f.close()
        
if __name__=="__main__":
    fileList = ["article_000.txt","article_001.txt","article_002.txt","article_003.txt","article_004.txt","article_005.txt"]
    map(readFile,fileList)
    word_freq = sorted(word_freq_list.iteritems(),key=lambda d:d[1],reverse=True)
    print u"常用单词前十"
    i=0
    for w in word_freq:
        print w[0]+"\t",w[1]
        i += 1
        if i==10:
            break
    
        