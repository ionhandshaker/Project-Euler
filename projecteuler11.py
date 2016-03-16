# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:40:00 2015

@author: Nandhakishore
"""

#f=open("eulerproblem11.txt","r")
#main=f.read()
#main=int(main)
with open("eulerproblem11.txt") as f:
    data = [map(int,line.split()) for line in f]

large_number=[]
index=[]
maximum=0

for i in range(0,20):
    for j in range(0,20):
        if(j<=16):
            prod=data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3]
            #prod1=data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j]
            
            if(prod>maximum):
                maximum=prod
                #index.append(i)
                #index.append(j)
           # if(prod1>maximum):
            #    maximum=prod1
large_number.append(maximum)

maximum=0
for i in range(0,20):
    for j in range(0,20):
        if(i<=16):
            prod=data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j]
            #maximum=0
            if(prod>maximum):
                maximum=prod
                index.append(i)
                index.append(j)

large_number.append(maximum)


maximum=0
for i in range(0,20):
    for j in range(0,20):
        if(i<=16 and j<=16):
            prod=data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3]
            
            if(prod>maximum):
                maximum=prod
                #index.append(i)
                #index.append(j)
large_number.append(maximum)

maximum=0
for i in range(0,20):
    for j in range(0,20):
        if(j>=3 and i<=16):
            prod=data[i][j]*data[i+1][j-1]*data[i+2][j-2]*data[i+3][j-3]
            
            if(prod>maximum):
                maximum=prod
                #index.append(i)
                #index.append(j)
large_number.append(maximum)

