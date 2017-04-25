# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:01:43 2016

@author: Nandhakishore
"""

string_array=[]
for i in range(1,500000):
    c=str(i)
    for j in range(0,len(c)):
        string_array.append(c[j])
    