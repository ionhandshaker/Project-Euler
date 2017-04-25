# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:38:39 2016

@author: Nandhakishore
"""

required=[]
for i in range(1,4000):
    for j in range(1,4000):
        n=i*j
        if(len(str(n)+str(i)+str(j))==9):
            tot=[]
            together=str(n)+str(i)+str(j)
            for ch in range(9):
                tot.append(int(together[ch]))
            req=set(tot)
            req=list(req)
            if(sum(req)==45):
                required.append(n)
                #print i,j,n

required=set(required)
required=list(required)
print sum(required)


"""
final=set(required)
final=list(final)
print sum(final)
"""