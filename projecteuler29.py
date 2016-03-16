# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 23:43:04 2016

@author: Nandhakishore
"""
array=[]
for a in range(2,101):
    for b in range(2,101):
        x=a**b
        array.append(x)
        
required=set(array)
required=list(required)

print len(required)
        