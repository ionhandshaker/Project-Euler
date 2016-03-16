# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 22:19:58 2016

@author: Nandhakishore
"""
#Code based on Fermat's Little Theorem
import math
def isPrime(n):
    if(n==1):
        return False
    elif(n<4):
        return True
    elif(n%2==0):
        return False
    elif(n%3==0):
        return False
    elif(n<10):
        return True
    else:
        r=math.sqrt(n)
        r=math.floor(r)
        f=5
        while(f<=r):
            if(n%f==0):
                return False
                break
            elif(n%(f+2)==0):
                return False
                break
            f=f+6
        return True
        
prime=[]
for i in range(1,1000):
    if(isPrime(i)):
        prime.append(i)
  
maximum=0      
for j in range(1,len(prime)):
    #k=1
    for k in range(1,1000):
        num=(10**k)-1
        if(num%prime[j]==0):
            cycle=k
            break
        #k=k+1
    if(cycle>maximum):
        maximum=cycle
        answer=prime[j]

print answer

"""
This problem is solved based on Fermat's Little theorem which states that
(1/d) has a cycle of n digits if ((10^n)-1)mod(d)==0 if d is prime.
And composite numbers have small recurring cycles.
"""

        
        
        