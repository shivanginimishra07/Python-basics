# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:54:36 2020

@author: itssh
"""

dict={}
string=input()
print(5)
temp=0
for i in string:
    keys=dict.keys()
    if i in keys:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
        