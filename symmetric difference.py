# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:18:59 2020

@author: itssh
"""
m,n,a,b=int(input().split())
x=set(b)
y=set(a)
p=x.difference(y)
q=y.difference(x)
r=p.union(q)
print('\n'.join(sorted(r,key=int)))
