# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:54:35 2015

@author: Nandhakishore
"""

def isPalindrome(n):
    if(n==int(str(n)[::-1])):
        return 1
    else:
        return 0
arr=[]
for j in range(100,999):
    for i in range(100,999):
        prod=i*j
        if(isPalindrome(prod)==1):
            arr.append(prod)

print max(arr)
    