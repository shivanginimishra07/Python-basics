# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:08:05 2020

@author: itssh
"""
ls1=[]
n=int(input('enter the size of the the list'))
ls2=[]
for i in range(0,n):
    ele=input()
    if ele==ele[::-1]:
        ls1.append(ele)
        ls2=ls1[:]
print(ls2)
