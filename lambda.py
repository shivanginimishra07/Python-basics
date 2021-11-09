# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:45:28 2020

@author: itssh
"""
x=int(input())
y=int(input())
a=lambda x,y:x+y
b=lambda x,y:x-y
print(a(x+y)-b(x-y))