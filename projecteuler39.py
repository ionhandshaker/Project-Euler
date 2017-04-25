# -*- coding: utf-8 -*-
"""
Created on Sun May 08 02:47:31 2016

@author: Nandhakishore
"""
check=0

#required=[]
for p in range(1,1001):
    required=[]
    for a in range(1,p):
        for b in range(1,a):
            c=p-a-b
            if(a>0 and b>0 and c>0):
                if(a**2==b**2+c**2):
                    required.append((a,b,c))
                    if(len(required)>check):
                        final=required
                        check=len(required)
                        want=p