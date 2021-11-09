# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:18:45 2019

@author: itssh
"""

from tkinter import Label
master=Tk()
l1=Label(master,text="Do you think Shivam is ugly",font=("pristina",50))
l1.grid(column=0,row=0)
def clicked():
    l1.configure(text="Yes!You are absolutely correct")
button=Button(master,text="Yes",command=clicked)
button.grid(column=1,row=0)
def cliked():
    l1.configure(text="Oops!You are wrong.")
butt=Button(master,text="No",command=cliked)
butt.grid(column=1,row=1)
txt=Entry()
mainloop()