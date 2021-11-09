# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:49:55 2019

@author: itssh
"""

import heapq
grades=[110,25,38,49,20,49,87,80,90]
print(heapq.nlargest(3,grades))
print(heapq.nsmallest(4,grades))