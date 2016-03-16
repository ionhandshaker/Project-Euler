# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:58:40 2015

@author: Nandhakishore
"""

def isPrime(n):
    j=2
    while(j>=2 and j<n):
        if(n%j==0):
            check=0
            break
        else:
            check=1
        j=j+1
    return check
main=600851475143
k=main-1
while(k>0):
    a=isPrime(k)
    if(a==1 and main%k==0):
        print(a)
    break
    k=k-1
    
    