# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:29:30 2020

@author: itssh
"""

num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=sum
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")