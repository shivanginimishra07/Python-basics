# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:24:16 2020

@author: itssh
"""

from collections import deque
d=deque()
n=int(input())
for _ in range(int(input())):
    method,*n=input().split()
    getattr(d,method)(*n)
print(*d)