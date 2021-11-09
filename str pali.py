# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:58:22 2019

@author: itssh
"""

s=input("enter a string")
x=""
for i in s[-1::-1]:
    x=x+i
if x==s:
    print("pali")
