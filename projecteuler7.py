# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 11:46:31 2015

@author: Nandhakishore
"""

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            check=0
            break
        else:
            check=1
    return check

index=2
for j in range(1,100000):
    first_test=6*j-1
    second_test=6*j+1
    check1=isPrime(first_test)
    check2=isPrime(second_test)
    if(check1==1):
        index=index+1
    if(check2==1):
        index=index+1
    if(index==10001):
        print j
        break