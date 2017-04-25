# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 16:16:25 2016

@author: Nandhakishore
"""

def is_pentagonal(n):
    disc=1+4*3*2*n
    disc=disc**0.5
    x=(1+disc)/6
    if(x-int(x)==0):
        return True
    else:
        return False

def is_hexagonal(n):
    disc=1+4*2*n
    disc=disc**0.5
    x=(1+disc)/4
    if(x-int(x)==0):
        return True
    else:
        return False
        
        
count=0
for i in range(286,100000):
    tri=i*(i+1)/2
    if(is_pentagonal(tri) and is_hexagonal(tri)):
        count+=1
        if(count==1):
            break