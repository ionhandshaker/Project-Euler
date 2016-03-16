# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:24:56 2015

@author: Nandhakishore
"""

#import num2word
single_digit=['one','two','three','four','five','six','seven','eight','nine','']
teens=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def num2word(x):
    if(x>0 and x<10):
        out=single_digit[x-1]
    if(x>10 and x<20):
        out=teens[x-11]
    
    if(x==10):
        out=tens[0]
    
    if(x>=20 and x<100):
        #out=tens[int(str(x)[1])]+single_digit[int(str(x)[0])]
        out=tens[int(str(x)[0])-1]+single_digit[int(str(x)[1])-1]
        
    if(x==100):
        out='onehundred'
    """
    if(x>100 and x<1000):
        out=single_digit[int(str(x)[0])-1]+'hundredand'+tens[int(str(x)[1])-1]+single_digit[int(str(x)[2])-1]
    """
    if(x>100 and x<1000):
        out=single_digit[int(str(x)[0])-1]+'hundredand'+tens[int(str(x)[1])-1]+single_digit[int(str(x)[2])-1]
        if(int(str(x)[1])==0):
            out=single_digit[int(str(x)[0])-1]+'hundredand'+single_digit[int(str(x)[2])-1]
        #new=single_digit[int(str(x)[0])-1]
        #print "Hello"
        if(int(str(x)[1])==1):
            out=single_digit[int(str(x)[0])-1]+'hundredand'+teens[int(str(x)[2])-1]
            if(int(str(x)[1])==1 and int(str(x)[2])==0):
                out=single_digit[int(str(x)[0])-1]+'hundredandten'
        
        if(x%100==0):
            out=single_digit[int(str(x)[0])-1]+'hundred'

    return out

count=len('onethousand')
#count=0
for i in range(1,1000):
    count=count+len(num2word(i))
#x=486

        
    
    