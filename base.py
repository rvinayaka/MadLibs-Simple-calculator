from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Learn")

# root.iconbitmap("/home/bc2113451/Desktop/icon.ico")


def open():
    top = Toplevel()        #? for creating two window
    top.title("Second window")

    #lbl = Label(top, text = "This is a new window").pack()
    global img
    img = ImageTk.PhotoImage(Image.open("/home/bc2113451/Desktop/paws.png"))   
    lbl = Label(top, image = img).pack()
    Button(top, text = "Quit", command = top.destroy).pack()

btn = Button(root, text = "Open second window", command = open).pack()

root.mainloop()