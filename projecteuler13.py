# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:56:57 2015

@author: Nandhakishore
"""
"""
with open("eulerproblem13.txt") as f:
    data = [map(int,line.split()) for line in f]
"""
data=[]
for line in open("eulerproblem13.txt"):
   if line.strip():           # line contains eol character(s)
       n = int(line)
       data.append(line)          # assuming single integer on each line
add=0
#add1=0
last_digit=[]
"""
for j in range(50,0,-1):
    for i in range(0,99):
        add=add+int(str(data[i])[j])
    #add=int(str(add)[0:2])
    if(j<=10):
        last_digit.append(int(str(add)[2]))
    add=int(str(add)[0:2])
"""

#add=int(str(data[0])[50])+int(str(data[1])[50])

"""
for j in range(50,0,-1):
    for i in range(0,5):
        add=add+int(str(data[i])[j])
    """
"""
    if(j<=8):
        last_digit.append(int(str(add)[len(str(add))-1]))
    """
"""
    #add=int(str(add)[0:len(str(add))-1])
    add=str(add)[0:len(str(add))-1]
"""

#f=sum(data)
"""
for j in range(50,0,-1):
    for i in range(0,5):
        add=add+int(str(data[i])[j])
    last_digit.append(int(str(add)[len(str(add))-1]))
    add=str(add)[0:len(str(add))-1]

"""
"""
for i in range(0,100):
    add=add+int(data[i])
"""    

#list1=map(int,data)
data = [int(i) for i in data]
#a=37107287533902102798797998220837590246510135740250L
"""
for i in range(0,100):
    add1=add1+int(data[i])
"""

for j in range(49,-1,-1):
    for i in range(0,100):
        add=add+int(str(data[i])[j])
    #add=int(str(add)[0:2])
    if(j<=10):
        last_digit.append(int(str(add)[2]))
    add=int(str(add)[0:2])



