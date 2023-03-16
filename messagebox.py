from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')

def info():
    messagebox.showinfo("This is info tab", "Hello World !!")

def warning():
    messagebox.showwarning("This is warning tab", "Hello World !!")

def error():
    messagebox.showerror("This is error tab", "Hello World !!")

def question():
    messagebox.askquestion("This is a question tab", "Hello World !!")

def okcancel():
    messagebox.askokcancel("This is ok cancel tab", "Hello World !!")

def yesno():
    messagebox.askyesno("This is yes no tab", "Hello World !!")

#$ showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

#^ showinfo -> OK
#^ showwarning -> OK for warning
#^ showerror -> OK for error
#^ askquestion -> YES / NO
#^ askokcancel -> OK / CANCEL
#^ askyesno -> YES / NO

Button(root, text = "Open info", command = info).pack()

Button(root, text = "Open warning", command = warning).pack()

Button(root, text = "Open error", command = error).pack()

Button(root, text = "Open question", command = question).pack()

Button(root, text = "Open cancel", command = okcancel).pack()

Button(root, text = "Open yes/no", command = yesno).pack()
root.mainloop()









