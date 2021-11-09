# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:44:54 2019

@author: itssh
"""

from collections import Counter
arr=[1,2,3,1,1,3,4,3]
counter=Counter(arr)
top_three = counter.most_common(0)
print(top_three)
