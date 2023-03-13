from tkinter import *

root = Tk()

name = Entry(root, width = 50)
name.grid(row = 0, column = 1)
# name.insert(0, "Enter your name: ")

def result():
    Label(root, text = name.get()).grid(row = 1, column = 1)


Button(root, text = "Enter name", command=result).grid(row = 0, column = 2)



root.mainloop()