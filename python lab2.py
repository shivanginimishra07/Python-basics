# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:29:17 2020

@author: itssh
"""

age=input("enter age:")
if age>=18:
    print("you are eligible")
else:
    print("you are not eligible by {}years".format(18-age))