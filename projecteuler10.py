# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:11:54 2015

@author: Nandhakishore
"""
import math

#def isPrime(n):
""" for i in range(2,n):
        if(n%i==0):
            check=0
            break
        else:
            check=1
    return check
"""
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
            elif(n%(f+2)==0):
                return False
                break
            f=f+6
        return True

#index=2

total=0
for j in range(1,2000000):
    if(isPrime(j)):
        total=total+j
print total

"""
    if(check1==1):
        index=index+1
    if(check2==1):
        index=index+1
    if(index==10001):
        print j
        break
"""