# -*- coding: utf-8 -*-
"""
Created on Sun May 01 03:09:43 2016

@author: Nandhakishore
"""

required=[]
for i in range(10,99):
    for j in range(i+1,100):
        a=[str(i)[0],str(i)[1]]
        b=[str(j)[0],str(j)[1]]
        common=list(set(a)& set(b))
        if(len(common)==1):
            if(int(common[0])!=0):
                #strike1=a.index(common[0])
                a.remove(common[0])
                b.remove(common[0])
                if(float(b[0])!=0):
                    if(float(a[0])/float(b[0])==float(i)/float(j)):
                        required.append((a[0],b[0]))

"""
i=10
j=11
a=[str(i)[0],str(i)[1]]
b=[str(j)[0],str(j)[1]]
common=list(set(a)&set(b))
a.remove(common[0])
b.remove(common[0])
x=float(a[0])/float(b[0])
"""              