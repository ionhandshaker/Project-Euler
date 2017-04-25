# -*- coding: utf-8 -*-
"""
Created on Sat Sep 03 00:05:24 2016

@author: Nandhakishore
"""

import math
def isPrime(n):
    if(n==1):
        return False
    elif(n<4):
        return True
    elif(n%2==0):
        return False
    elif(n<9):
        return True
    elif(n%3==0):
        return False
    else:
        f=5
        r=math.sqrt(n)
        r=math.floor(r)
        while(f<=r):
            if(n%f==0):
                return False
                break
            if(n%(f+2)==0):
                return False
                break
            f=f+6
        return True

i=3
count=0
while i<1000:
    for j in range(1,i):
        x=i-2*(j**2)
        if(isPrime(x)):
            break
        else:
            count+=1
    if(count==i-1):
        req=i
        break
    i=i+2
    
