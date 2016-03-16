# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 22:10:51 2015

@author: Nandhakishore
"""
"""
k=1
#i=1
while(k>0):
    if(k%2==0 and k%3==0 and k%4==0):
        if(k%5==0 and k%6==0 and k%7==0):
            if(k%8==0 and k%9==0 and k%10==0):
                if(k%11==0 and k%12==0 and k%13==0):
                    if(k%14==0 and k%15==0 and k%16==0):
                        if(k%17==0 and k%18==0 and k%19==0 and k%20==0):
                            print k
                            break
    k=k+1
"""
"""
n=1
for i in range(1,11):
    n=n*i
      #n=n*i
print n 
"""
#k=2
"""
sum=0
for k in range(1,10000000):
    #if()
    for i in range(1,20):
        if(k%i==0):
            sum=sum+i
            if(sum==210):
                print k
                break
"""
"""
k=1
while(k>0 and k<10000):
    for i in range(2,20):
        if(k%i==0):
            while(i==20):
#            
                print k
                break 
           # break
        else:
            k=k+1
"""
"""
def check_divisibility(n):
    i=1
    while(n%i==0):
   #     n=n/i
        i=i+1
        if(i==10):
            check=1            
            break
        else:
            check=0
    return check
"""

"""
#k=1
for k in range(1,10000):
    test=check_divisibility(k)
    if(test==1):
        print k
        break
   """             
 """    
def check_for(n):
    i=11
    while(n%i==0):
        i=i+1
        if(i==20):
            check=1
            break
        else:
            check=0
        return check
     """
     
#solution based on minimum number of primes required
        