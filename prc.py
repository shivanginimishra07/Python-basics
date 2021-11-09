# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:54:06 2019

@author: itssh
"""

from tkinter import Spinbox
window=Tk()
spin=Spinbox(window,from_=0,to=100,width=5)
spin.grid(column=5,row=5)
mainloop()