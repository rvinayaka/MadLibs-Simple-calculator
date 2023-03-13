from tkinter import *

root = Tk()
root.title("Simple lambda: calc(2)ulator")

number = Entry(root, width = 30, borderwidth = 5)
number.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def calc(num):
    previous = number.get()                         #! getting the input                            input = 1
    number.delete(0, END)                           #! deleting the number typed before             5 already typed so deleting it
    number.insert(0, str(previous) + str(num))      #! adding the previous and current number       adding "1" and "5" ==>> 15


def clear():
    number.delete(0, END)


def addition():
    first_num = number.get()            #$ getting the first number for calculation
    
    global math                         #! greating global function for operations
    math = "addition"
    
    global f_num                        #^ creating global number
    f_num = int(first_num)              
    number.delete(0, END)               #$ deleting first number to add second number
    

def substraction():
    first_num = number.get()

    global math
    math = "substraction"

    global f_num
    f_num = int(first_num)

    number.delete(0, END)


def multiplication():
    first_num = number.get()
    
    global math
    math = "multiplication"

    global f_num                        
    f_num = int(first_num)

    number.delete(0, END)


def division():
    first_num = number.get()

    global math
    math = "division"

    global f_num
    f_num = int(first_num)

    number.delete(0, END)



def equal():
    second_num = number.get()
    number.delete(0, END)

    if math == "addition":
        number.insert(0, f_num + int(second_num))


    elif math == "substraction":
        number.insert(0, f_num - int(second_num))


    elif math == "multiplication":
        number.insert(0, f_num * int(second_num))


    elif math == "division":
        number.insert(0, f_num / int(second_num))


#^ Define the buttons
button_1 = Button(root, text = "1", padx = 43, pady = 20, command= lambda: calc(1))             #! using lamda function to pass arguments
button_2 = Button(root, text = "2", padx = 43, pady = 20, command= lambda: calc(2))
button_3 = Button(root, text = "3", padx = 43, pady = 20, command= lambda: calc(3))
button_4 = Button(root, text = "4", padx = 43, pady = 20, command= lambda: calc(4))
button_5 = Button(root, text = "5", padx = 43, pady = 20, command= lambda: calc(5))
button_6 = Button(root, text = "6", padx = 43, pady = 20, command= lambda: calc(6))
button_7 = Button(root, text = "7", padx = 43, pady = 20, command= lambda: calc(7))
button_8 = Button(root, text = "8", padx = 43, pady = 20, command= lambda: calc(8))
button_9 = Button(root, text = "9", padx = 43, pady = 20, command= lambda: calc(9))
button_0 = Button(root, text = "0", padx = 43, pady = 20, command= lambda: calc(0))

button_add = Button(root, text = "+", padx = 40, pady = 20, command = addition)
button_substract = Button(root, text = "-", padx = 43, pady = 20, command = substraction)
button_multiply = Button(root, text = "*", padx = 43, pady = 20, command = multiplication)
button_divide = Button(root, text = "/", padx = 43, pady = 20, command = division)

button_equal = Button(root, text = "=", padx = 90, pady = 20, command = equal)
button_clear = Button(root, text = "Clear", padx = 79, pady = 20, command = clear)


#^ Put the buttons on the screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 2)

button_add.grid(row = 5, column = 0)
button_substract.grid(row = 6, column = 2) #, columnspan=3)
button_multiply.grid(row = 6, column = 1) #, columnspan=3)
button_divide.grid(row = 6, column = 0) #, columnspan=3)
button_equal.grid(row = 5, column = 1, columnspan = 2)

root.mainloop()