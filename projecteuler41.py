# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 02:57:06 2016

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


great=0
l=[1,2,3,4,5,6,7]
import itertools
g=itertools.permutations(l)
g=list(g)

for i in range(0,len(g)):
    new=''
    for j in range(0,len(l)):
        new=new+str(g[i][j])
    #print int(new)
    
    if(isPrime(int(new))):
        if(int(new)>great):
            great=int(new)
        
