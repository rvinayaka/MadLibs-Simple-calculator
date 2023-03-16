from tkinter import *
from PIL import ImageTk, Image  

root = Tk()
# root.iconbitmap('@/home/bc2113451/Pictures/chess.xbm')

root.title("Hey open")

img1 = ImageTk.PhotoImage(Image.open("/home/bc2113451/Desktop/projects/paws.png"))
img2 = ImageTk.PhotoImage(Image.open("/home/bc2113451/Pictures/naruto.jpg"))
img = ImageTk.PhotoImage(Image.open("/home/bc2113451/Pictures/itachi.png"))

label = Label(root, image = img).pack()
label1 = Label(root, image = img1).pack()
label2 = Label(root, image = img2).pack()

exit = Button(root, text = "exit", command=root.quit).pack()

root.mainloop()