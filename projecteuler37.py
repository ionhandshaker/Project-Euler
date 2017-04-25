# -*- coding: utf-8 -*-
"""
Created on Mon May 02 13:29:40 2016

@author: Nandhakishore
"""

import math

def is_prime(n):
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
            elif(n%(f+2)==0):
                return False
                break
            f=f+6
        return True

required=[]
for i in range(1,1000000):
    if(is_prime(i)):
        x=len(str(i))
        count1=0
        for j in range(x):
            k=str(i)[j:x]
            if(not is_prime(int(k))):
                break
            count1+=1
        count2=0
        for m in range(x):
            k=str(i)[0:(x-m)]
            if(not is_prime(int(k))):
                break
            count2+=1
        if(count1==x and count2==x):
            required.append(i)




