# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:50:10 2020

@author: itssh
"""

n1=input("enter the first number")
n2=input("enter the second number")
n3=input("enter the third number")
if n1>n2 and n1>n3:
    print("the greatest number is {}".format(n1))
elif n2>n1 and n2>n3:
    print("the greatest number is {}".format(n2))
else: 
    print("the greatest number is {}".format(n3))