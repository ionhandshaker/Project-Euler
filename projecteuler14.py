# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:17:48 2015

@author: Nandhakishore
"""

#n=input()
maximum=0
for n in range(1,1000000):
    total=[]
    total.append(n)
    while(n!=1):
        if(n%2==0):
            n=n/2
            total.append(n)
        else:
            n=3*n+1
            total.append(n)
    l=len(total)
    if(l>maximum):
        maximum=l
        number=total[0]