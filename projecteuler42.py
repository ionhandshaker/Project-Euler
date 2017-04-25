# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:48:21 2016

@author: Nandhakishore
"""

data=[]
for line in open("eulerproblem42.txt"):
   if line.strip():           # line contains eol character(s)
       #n = int(line)
       data.append(line)          # assuming single integer on each line

data=data[0].split(",")
data=[data[word].strip('"') for word in range(len(data))]


count=0

for i in range(0,len(data)):
    string_count=0
    for j in range(0,len(data[i])):
        string_count=string_count+ord(data[i][j])-64
    k=1
    while(k<26):
        if(string_count*2==k*(k+1)):
            count=count+1
            break
        k=k+1







