# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:02:29 2019

@author: itssh
"""

from tkinter import *
master=Tk()
w=Canvas(master,width=40,height=60)
w.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/4)
w.create_line(0,y,canvas_width,y)
mainloop()