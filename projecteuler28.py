# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 00:16:59 2016

@author: Nandhakishore
"""
"""
import math
array=[]
for i in range(5):
    x=[0 for j in range(5)]
    array.append(x)
   
   
to_fill=[k for k in range(1,26)]   
i=2
j=2
k=0
for k in range(25):
    array[i][j]=to_fill[k]
    if((math.sqrt(array[i][j])%1)==0):
        array
"""
total=0
#array=[]
n=1001       
for i in range(1,n+1):
    if(i%2==1):
       total=total+i**2
       #array.append(i**2)
       if(i!=n):
           total=total+(i**2+i+1)
           #array.append()
    else:
        total=total+(i**2+1)+(i**2+i+1)
    
print total
    
    
    
