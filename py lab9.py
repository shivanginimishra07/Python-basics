# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:39:58 2020

@author: itssh
"""

number=int(input("please enter the number:"))
sum=0
while(number>0):
    reminder=number%10
    sum+=reminder
    number=number//10
    
print("sum of the digits of given number is=%d"%sum)