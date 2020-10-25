# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:05:53 2020

@author: 66IN
"""

from tkinter import *
import webbrowser
root = Tk()

root.title("Search: ")

def search():
    url = e.get()
    webbrowser.open(url)
    

label1 = Label(root,text="URL", font=("arial",10,"bold"))
label1.grid(row=0,column=0)

e = Entry(root,width=30)
e.grid(row=0,column=1)

button = Button(root, text= "Search",command=search)
button.grid(row=1,column=0,columnspan=2,pady=10)



root.mainloop()