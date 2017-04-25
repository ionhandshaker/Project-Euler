# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 01:17:19 2016

@author: Nandhakishore
"""
"""
required=200
coins=[1,2,5,10,20,50,100,200]
def count(n,m):
    if n<0 and m<=0:
        return 0
    if n==0:
        return 1
    return count(n,m-1)+count(n-coins[m],m)
    
count(required,7)
"""

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        #print ways[i]
        ways[i] += ways[i-coin]

print "Ways to make change =", ways[target]