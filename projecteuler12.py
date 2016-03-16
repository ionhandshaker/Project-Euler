# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 21:14:54 2015

@author: Nandhakishore
"""

def factor_length(n):
    factors=[]
    r=pow(n,0.5)
    r=int(r)
    for i in range(2,r+1):
        if(n%i==0):
            factors.append(i)
            if(i!=r):
                factors.append(n/i)
    #return factors
    return len(factors)+2
    
"""
for i in range(2,50000):
    triangular_no=i*(i+1)/2
    if(factor_length(triangular_no)==500):
        print triangular_no
        break
"""    

def required(req):
    triang=req*(req+1)/2
    return factor_length(triang)
    
for i in range(0,50000):
    if(required(i)>500):
        print i
        break
            