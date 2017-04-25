# -*- coding: utf-8 -*-
"""
Created on Mon May 02 03:08:38 2016

@author: Nandhakishore
"""

def is_palindrome(n):
    if(n==n[::-1]):
        return True
    else:
        return False

tot=0        
for i in range(1,1000000):
    if(is_palindrome(str(i)) and is_palindrome(bin(i)[2:len(bin(i))])):
        tot+=i
        
