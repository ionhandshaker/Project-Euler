# -*- coding: utf-8 -*-
"""
Created on Fri Sep 02 15:22:51 2016

@author: Nandhakishore
"""

def is_pentagonal(n):
    disc=1+4*3*2*n
    disc=disc**0.5
    x=(1+disc)/6
    if(x-int(x)==0):
        return True
    else:
        return False
        
count=0   

def modulus(n):
    if(n>=0):
        return n
    else:
        return -n
     

for j in range(1,10000):
    for k in range(1,10000):
        p_j=j*(3*j-1)/2
        p_k=k*(3*k-1)/2
        if(is_pentagonal(p_j+p_k) and is_pentagonal(modulus(p_j-p_k))):
            #print p_j+p_k
            #break
            count=count+1
            #print 'Hello'
            if(count==1):
                a=j
                b=k
                break

"""
j=1
k=1
while(j<10):
    while(k<10):
        p_j=j*(3*j-1)/2
        p_k=k*(3*k-1)/2
        if(is_pentagonal(p_j+p_k)):
            print p_j+p_k
        break
        k=k+1
    j=j+1
"""
 