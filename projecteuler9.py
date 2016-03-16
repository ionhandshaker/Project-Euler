# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:36:08 2015

@author: Nandhakishore
"""

for i in range(1,500):
    for j in range(1,500):
        if(i**2+j**2==(1000-(i+j))**2):
            print i,j
            