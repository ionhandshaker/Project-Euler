# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:23:07 2015

@author: Nandhakishore
"""

huge_number="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
prod_arr=[]
prod=1
#k=0
"""
for i in range(0,76):
    for j in range(0,13):
        prod=prod*int(huge_number[k+j])
        prod_arr.append(prod)
        k=k+1
"""
"""
for i in range(0,13):
    prod=prod*int(huge_number[i])
prod_arr.append(prod)
count=0
for j in range(13,1000):
    if(int(huge_number[j-13])==0):
        count=count+1 
    else:
        prod=prod*int(huge_number[j])/int(huge_number[j-13])
        print(prod)
        prod_arr.append(prod)
"""
"""
#for i in range(0,):
for j in range(0,13):
    prod=prod*int(huge_number[k+j])
    prod_arr.append(prod)
    k=k+1
"""
"""
while(k>=0 and k<987):
    for j in range(0,13):
        prod=prod*int(huge_number[k+j])
    prod_arr.append(prod)
    k=k+1
"""
"""
while(k>=0 and k<988):
    for i in range(0,13):
        prod1=prod*int(huge_number[k+i])
    prod_arr.append(prod1)
    k=k+1
"""
#prod=int(huge_number[0])*int(huge_number[1])*int(huge_number[2])*int(huge_number[3])*int(huge_number[4])*int(huge_number[5])*int(huge_number[6])*int(huge_number[7])*int(huge_number[8])*int(huge_number[9])*int(huge_number[10])*int(huge_number[11])*int(huge_number[12])
#prod=1

for k in range(0,988):
    for j in range(0,13):
        prod=prod*int(huge_number[k+j])
    prod_arr.append(prod)
    prod=1

"""
k=14
for j in range(0,13):
    prod=prod*int(huge_number[k+j])
"""