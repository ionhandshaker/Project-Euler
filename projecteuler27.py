# -*- coding: utf-8 -*-
"""
Created on Sat Jan 09 00:30:39 2016

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
        
maximum=0 
"""       
for i in range(1,1001):
    for j in range(1,1001):
        for n in range(0,1000):
            d1=n**2+i*n+j
            #d2=n**2-i*n+j
            #d3=n**2+i*n-j
            #d4=n**2-i*n-j
            if(isPrime(d1)):
                if(n>maximum):
                    maximum=n
                    a=i
                    b=j
"""
prime=[]
for k in range(1,1001):
    if(isPrime(k)):
        prime.append(k)
             
"""       
for i in range(1,1001):
    for j in range(0,len(prime)):
        for n in range(0,1000):
            d=n**2+i*n+j
            if(isPrime(d)):
                if(n>maximum):
                    maximum=n
                    a=i
                    b=prime[j]
"""              
"""
for i in range(1,16):
    for j in range(0,len(prime)):
        for n in range(0,50):
            d=n**2+i*n+prime[j]
            if(isPrime(d) and isPrime):
                if(n>maximum):
                    maximum=n
                    a=i
                    b=prime[j]
"""

for i in range(1,1000):
    for j in range(0,len(prime)):
        count=0
        n=0
        #print i,j,n
        while(n>=0):
            d=n**2-i*n+prime[j]
            if(d>0):
                if(isPrime(d)):
                    count=count+1       
                else:
                    break
            
            n=n+1
        if(count>maximum):
            maximum=count
            a=i
            b=prime[j]

print -(a*b)

"""
Haven't included n^2+i*n+prime[j]. a=1 and b=41 when a is positive
"""

#for j in range(0,len(prime)):
        








          
            