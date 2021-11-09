# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:08:10 2020

@author: itssh
"""

def simmple(**arg):
    if arg["snr"]==True:
        retuen (arg["principal"]+(arg["yrs"]*10))
    else:
        retuen arg["principal"]+(arg["yrs"]*12)
s=bool(input("enter true if snr citizen else false"))
p=int(input("enter principal amt"))
y=int(input("enter the number of years"))
print("simple intrest is",simpe(snr=s,principal=p,yrs=y))