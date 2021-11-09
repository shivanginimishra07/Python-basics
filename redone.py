# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:59:32 2020

@author: itssh
"""

dict={}
string=input()
for i in string:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
        