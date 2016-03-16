# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:30:37 2015

@author: Nandhakishore
"""

import math

def isAbundant(n):
    divisors=[]
    r=pow(n,0.5)
    r=int(math.floor(r))
    for i in range(1,r+1):
        if(n%i==0):
            divisors.append(i)
            if(i!=(n/i)):
                divisors.append(n/i)
    if((sum(divisors)-n)>n):
        return True
    else:
        return False
    
abundant=[]
for i in range(1,28124):
    if(isAbundant(i)):
        abundant.append(i)
"""        
for i in range(1,28124):
    for j in range(len(abundant)):
        for k in range(len(abundant)):
"""    
     
dont_require=[]
for i in range(len(abundant)):
    for j in range(len(abundant)):
        x=abundant[i]+abundant[j]
        if(x<28124):
            dont_require.append(x)

dont_require=set(dont_require)
dont_require=list(dont_require)
total=[i for i in range(1,28124)]
require=[y for y in total if y not in dont_require]
print sum(require)

"""
sums=0
for i in range(1,28123):
    if not any( (i-a in abundant) for a in abundant ):
        sums += i
"""






