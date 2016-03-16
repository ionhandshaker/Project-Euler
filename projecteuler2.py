# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 09:28:29 2015

@author: Nandhakishore
"""

num1=1
num2=2
sum=0
k=1
tot=num1+num2
while(k>0 and tot<4000000):
    tot=num1+num2
    num1=num2
    num2=tot
    if(tot%2==0):
        sum=sum+tot
    k=k+1
        