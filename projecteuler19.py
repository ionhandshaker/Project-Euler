# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 19:58:34 2015

@author: Nandhakishore
"""

#guessing dates within January
"""
def number_of_days(x,y):
    days=0
    for j in range(x,y+1):
        if(j%4==0):
            days=days+366
        else:
            days=days+365
    return days

initial_date=1
def find_month(integer,year):
    if(year%4!=0):
        if(integer>=initial_date and integer<initial_date+31):
            output=0  #January
        if(integer>=initial_date+31 and integer<initial_date+59):
            output=1  #February
        if(integer>=initial_date+59 and integer<initial_date+90):
            output=2  #March
        if(integer>=initial_date+90 and integer<initial_date+120):
            output=3  #April
        if(integer>=initial_date+120 and integer<initial_date+151):
            output=4  #May
        if(integer>=initial_date+151 and integer<initial_date+181):
            output=5  #June
        if(integer>=initial_date+181 and integer<initial_date+212):
            output=6  #July
        if(integer>=initial_date+212 and integer<initial_date+243):
            output=7  #August 
        if(integer>=initial_date+243 and integer<initial_date+273):
            output=8  #September
        if(integer>=initial_date+273 and integer<initial_date+304):
            output=9  #October
        if(integer>=initial_date+304 and integer<initial_date+334):
            output=10  #November
        if(integer>=initial_date+334 and integer<initial_date+365):
            output=11
        if(integer==0):
            output=11
    else:
        if(integer>=initial_date and integer<initial_date+31):
            output=0  #January
        if(integer>=initial_date+31 and integer<initial_date+60):
            output=1  #February
        if(integer>=initial_date+60 and integer<initial_date+91):
            output=2  #March
        if(integer>=initial_date+91 and integer<initial_date+121):
            output=3  #April
        if(integer>=initial_date+121 and integer<initial_date+152):
            output=4  #May
        if(integer>=initial_date+152 and integer<initial_date+182):
            output=5  #June
        if(integer>=initial_date+182 and integer<initial_date+213):
            output=6  #July
        if(integer>=initial_date+213 and integer<initial_date+244):
            output=7  #August 
        if(integer>=initial_date+244 and integer<initial_date+274):
            output=8  #September
        if(integer>=initial_date+274 and integer<initial_date+305):
            output=9  #October
        if(integer>=initial_date+305 and integer<initial_date+335):
            output=10  #November
        if(integer>=initial_date+335 and integer<initial_date+366):
            output=11
        if(integer==0):
            output=11
    return output

days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months=['January','February','March','April','May','June','July','August','September','October','November','December']
#initial_date=1
initial_day='Monday'
final_date=number_of_days(1901,2000)
#final_date=367
count=0
i=days.index(initial_day)
today_date=0
current_year=1900
k=0
for j in range(initial_date,final_date+1):
    today=days[(i%7)]
    today_date=today_date+1
    
    #if(today=='Sunday'):
     #   count=count+1
    
    i=i+1
    current_month=months[find_month(k,current_year)]
    k=k+1
        
    if(months[find_month(k,current_year)]!=months[find_month(k-1,current_year)]):
        today_date=1
        current_month=months[find_month(k,current_year)]
"""
    #if(today_date==1 and today=='Sunday'):
        #count=count+1
"""
    if(current_month=='December' and today_date==31):
        #current_year=current_year+1
        k=0
    if(current_month=='January' and today_date==1):
        current_year=current_year+1
        #k=0
    if(today_date==1 and today=='Sunday'):
        count=count+1
    print current_year,current_month,today_date,today
 #The answer I get is 172. The right answer is 171.   
"""
import datetime
#x=datetime.date.today()
#y=datetime.date(1900,1,1).isoweekday()
count=0
for year in range(1901,2001):
    for month in range(1,13):
        if(datetime.date(year,month,1).isoweekday()==7):
            count=count+1



