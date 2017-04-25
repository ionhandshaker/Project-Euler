# -*- coding: utf-8 -*-
"""
Created on Sun May 01 17:38:35 2016

@author: Nandhakishore
"""

import math
import itertools

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
    #x=len(str(i))
    if(is_prime(i)):
        x=len(str(i))
        req_list=[]
        for j in range(x):
            req_list.append(str(i)[j])
        #subset=list(itertools.permutations(req_list,x))
        subset=[[req_list[i-j] for i in range(x)] for j in range(x)]
        count=0
        for h in range(len(subset)):
            k=''.join(subset[h])
            if(is_prime(int(k))):
                count=count+1
            else:
                break
        if(count==len(subset)):
            required.append(i)
        
        
        
        
        