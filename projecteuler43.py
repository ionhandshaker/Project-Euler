# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:04:27 2016

@author: Nandhakishore
"""

import itertools
l=[0,1,2,3,4,5,6,7,8,9]
g=itertools.permutations(l)
g=list(g)
prime=[2,3,5,7,11,13,17]
h=len(g)
m=len(l)

"""
for i in range(0,h):
    new=''
    for j in range(0,m):
        new=new+str(g[i][j])
    total_no=int(new)
"""
#count=0
total=[]
for i in range(0,h):
    #new=''
    count=0
    for j in range(0,7):
        new=str(g[i][j+1])+str(g[i][j+2])+str(g[i][j+3])
        new=int(new)
        if(new%prime[j]==0):
            count=count+1
            if(count==7):
                total.append(g[i])
        else:
            break
  
    