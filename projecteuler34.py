# -*- coding: utf-8 -*-
"""
Created on Sun May 01 17:11:32 2016

@author: Nandhakishore
"""

def factorial(n):
    if(n<=0):
        return 1
    else:
        return n*factorial(n-1)
 

required=[]       
for i in range(3,1000000):
    x=len(str(i))
    tot=0
    for j in range(x):
        want=factorial(int(str(i)[j]))
        tot=tot+want
    if(i==tot):
        required.append(i)
        