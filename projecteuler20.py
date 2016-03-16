# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 00:27:21 2015

@author: Nandhakishore
"""

def fact(n):
    #fact(1)=1
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

total=0
x=fact(100)
for i in range(len(str(x))):
    total=total+int(str(x)[i])




