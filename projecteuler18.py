# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 14:57:25 2015

@author: Nandhakishore
"""

data=[]
for line in open("eulerproblem18.txt"):
   if line.strip():           # line contains eol character(s)
       #n = int(line)
       data.append(line)          # assuming single integer on each line

"""
rows = []
with open('eulerproblem18.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
"""
working_data=[]
#working_data=rows
path=[]

for i in range(0,len(data)):
    arr=map(int,data[i].split())
    b=[0 for j in range(len(data)-len(arr))]
    working_data.append(arr+b)
"""
count=0
add=working_data[0][0]
i=0
j=0
path.append(add)
for i in range(0,len(working_data)-1):
    count=count+add
    add=max(working_data[i+1][j],working_data[i+1][j+1])
    path.append(add)
    j=working_data[i+1].index(add)
    #for j in range(0,len(working_data)):
        #path.append(max(working_data[i]))
        #count=count
"""

for i in range(len(working_data)-2,-1,-1):
    for j in range(0,len(working_data)-1):
        working_data[i][j]=working_data[i][j]+max(working_data[i+1][j],working_data[i+1][j+1])

print working_data[0][0] #final answer for project euler



