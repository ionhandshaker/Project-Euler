# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:51:46 2016

@author: Nandhakishore
"""
total=0
array=[]

for i in range(1,999999+1):
    b=str(i)
    x=0
    #x=int(b[0])**5+int(b[1])**5+int(b[2])**5+int(b[3])**5+int(b[4])**5
    for j in range(0,len(b)):
        x=x+int(b[j])**5
    if(x==i):
        total=total+i
        array.append(i)
print total-1