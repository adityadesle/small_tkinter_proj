# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:33:48 2020

@author: 66IN
"""

from tkinter import *
import wikipedia as wiki


root = Tk()
root.title("Wikipedia")


def search():
    query = e.get()
    result = wiki.summary(query , sentences = 5)
    txt.insert(END,result)



label1 = Label(root,text="Search Query: ")
label1.grid(row=0,column=0)


e = Entry(root, width=30)
e.grid(row=0,column=1,padx=1)

button = Button(root,text="Search",command=search)
button.grid(row=0, column=2, padx=5)

txt  = Text(root,width=50)
txt.grid(row=1,column=0,columnspan=3)

root.mainloop()