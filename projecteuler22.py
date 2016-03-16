# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:18:55 2015

@author: Nandhakishore
"""
"""
def count_sort(a):
    c=[0 for i in range(max(a)+1)]
    output_string=['-' for j in range(len(a)+1)]

    for j in range(0,len(a)):
        c[a[j]]=c[a[j]]+1

    for i in range(1,len(c)):
        c[i]=c[i]+c[i-1]

    for j in range(len(a)-1,-1,-1):
        output_string[c[a[j]]]=data[j]
        c[a[j]]=c[a[j]]-1
    output_string=output_string[1:]
    return output_string
"""
data=[]
for line in open("p022_names.txt"):
   if line.strip():           # line contains eol character(s)
       #n = int(line)
       data.append(line)          # assuming single integer on each line

data=data[0].split(",")
data=[data[word].strip('"') for word in range(len(data))]
#orig=data
"""
data1=data
array=[]
#row=[]

for i in range(len(data)):
    row=[]
    for j in range(len(data[i])):
        #row=[]
        x=ord(data[i][j])
        row.append(x)
    array.append(row)
length=0

"""
#for i in range(len(array)):
 #   a=len(array[i])
  #  if(a>length):
   #     length=a
"""

for i in range(len(array)):
    zero=[0 for j in range(11-len(array[i]))]
    array[i]=array[i]+zero
"""
data.sort()
def find_value(a):
    l=[]
    for i in range(len(a)):
        x=ord(a[i])-64
        l.append(x)
    return sum(l)

total=0
for j in range(len(data)):
    total=total+((j+1)*find_value(data[j]))







