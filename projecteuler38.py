# -*- coding: utf-8 -*-
"""
Created on Sat May 07 15:20:19 2016

@author: Nandhakishore
"""

def does_contain_all_digits(check):
    x=list(check)
    x=[int(k) for k in x]
    if(len(set(check))==9 and 0 not in x):
        return True
    else:
        return False



required=0
for i in range(1,10000):
    check=''
    for j in range(1,100):
        check=check+str(i*j)
        #print check
        if(len(check)==9):
            if(does_contain_all_digits(check)):
                if(int(check)>required):
                    required=int(check)
        if(len(check)>9):
            break