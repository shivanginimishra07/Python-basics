# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:38:21 2019

@author: itssh
"""

for i in range(2,10000):
    s1=0
    s2=0
    for j in range(1,int(i)):
        if i%j==0:
            s1=s1+j
    for k in range(1,int(s1)):
        if s1%k==0:
            s2=s2+k
    if s1>i or s1==s2:
        continue
    elif s2==i:
        print(s1,s2)
