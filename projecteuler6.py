# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 00:41:02 2015

@author: Nandhakishore
"""
import math
def difference_between(n):
    term1=n*(n+1)/2
    term1=math.pow(term1,2)
    term2=n*(n+1)*(2*n+1)/6
    diff=term1-term2
    return diff