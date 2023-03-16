from tkinter import *

root = Tk()
root.geometry("200x200")
root.title("learn to code")

# r = IntVar()
# r.set("2")


toppings = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion","Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in toppings:
    Radiobutton(root, text = text, variable = pizza, value = mode).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text = value).pack()

# Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
# Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

# output_label = Label(root, text = pizza.get()).pack()
output_button = Button(root, text = "Click Me!", command = lambda: clicked(pizza.get())).pack()

root.mainloop()