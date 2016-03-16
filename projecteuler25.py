# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 14:35:58 2015

@author: Nandhakishore
"""

a=1
b=1
fibonacci=[]
fibonacci.append(a)
fibonacci.append(b)
for i in range(0,10000000):
    new=a+b
    fibonacci.append(new)
    if(len(str(new))==1000):
        out=i+2
        break
    a=b
    b=new
print out+1