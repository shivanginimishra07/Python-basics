# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 20:45:43 2019

@author: itssh
"""

from tkinter import *
master=Tk()
sg=Checkbutton(master,text="A")
sg.grid(column=0,row=0)
def clicked():
    l1.configure(text="Yes!You are absolutely correct")
button=Button(master,text="Enter",command=clicked)
button.grid(column=1,row=0)
mainloop()