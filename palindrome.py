# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:54:38 2019

@author: itssh
"""

x=int((input("enter")))
copy=x
rev=0
while(x>0):
    rev=rev*10+x%10
    x=int(x/10)
if rev==copy:
    print("pali")
