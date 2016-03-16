# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:54:31 2015

@author: Nandhakishore
"""

import math

def find_divisors(n):
    divisors=[]
    r=pow(n,0.5)
    r=int(math.floor(r))
    for i in range(1,r+1):
        if(n%i==0):
            divisors.append(i)
            if(i!=(n/i)):
                divisors.append(n/i)
    return divisors

#n=input()
#if(r*r==n):
 #   divisors.append(r)
    #return divisors
total=0

for j in range(1,10000):
    new_no=sum(find_divisors(j))-j
    #if(new_no<10000):
    x=sum(find_divisors(new_no))-new_no
    if(x==j and j!=new_no):#second condition after and because we want to avoid d(a)=a cases specified in the problem
        total=total+j

"""
j=input()
new_no=sum(find_divisors(j))-j
if(new_no<10000):
    x=sum(find_divisors(new_no))-new_no
if(x==j):
    total=total+(new_no+j)
"""
            
            
            
            
            
            