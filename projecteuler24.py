# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:09:40 2015

@author: Nandhakishore
"""

def next_permutation(a):
    for j in range(len(a)-1,-1,-1):
        if(a[j-1]<a[j]):
            pivot=j-1
            break
    for i in range(len(a)-1,-1,-1):
        if(a[i]>a[pivot]):
            new=i
            break
    a[pivot],a[new]=a[new],a[pivot]
    new_array=a[(pivot+1):]
    new_array=new_array[::-1]
    a[(pivot+1):]=new_array
    return a

initial=[0,1,2,3,4,5,6,7,8,9]
for k in range(0,999999):
    out=next_permutation(initial)








