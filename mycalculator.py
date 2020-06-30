from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("My Calculator")
root.geometry("300x650")

e = Entry(root, width= 40, borderwidth=5)
e.grid(row =0, column=0, columnspan=3, padx=10, pady=10)


def click(number):
     current = e.get()
     e.delete(0, END)
     e.insert(0, str(current)+str(number))

def clear():
    e.delete(0, END)

def add():
    global first
    global  math
    math = "addition"
    first = e.get()
    e.delete(0, END)

def multiply():
    global first
    global math
    math = "multiplication"
    first = e.get()
    e.delete(0, END)

def division():
    global first
    global  math
    math = "division"
    first = e.get()
    e.delete(0, END)


def subtraction():
    global first
    global  math
    math = "subtraction"
    first = e.get()
    e.delete(0, END)


def equal():
    global sec
    sec = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, int(first)+int(sec))

    elif math == "multiplication":
        e.insert(0, int(first)*int(sec))

    elif math == "subtraction":
        e.insert(0, int(first)-int(sec))

    elif math == "division":
        e.insert(0, int(first)/int(sec))

b9= Button(root, text="9", padx=40, pady=40, command=lambda: click(9)).grid(row=1, column=2)
b8= Button(root, text="8", padx=40, pady=40, command=lambda: click(8)).grid(row=1, column=1)
b7= Button(root, text="7", padx=40, pady=40, command=lambda: click(7)).grid(row=1, column=0)
b6= Button(root, text="6", padx=40, pady=40, command=lambda: click(6)).grid(row=2, column=2)
b5= Button(root, text="5", padx=40, pady=40, command=lambda: click(5)).grid(row=2, column=1)
b4= Button(root, text="4", padx=40, pady=40, command=lambda: click(4)).grid(row=2, column=0)
b3= Button(root, text="3", padx=40, pady=40, command=lambda: click(3)).grid(row=3, column=2)
b2= Button(root, text="2", padx=40, pady=40, command=lambda: click(2)).grid(row=3, column=1)
b1= Button(root, text="1", padx=40, pady=40, command=lambda: click(1)).grid(row=3, column=0)
b0= Button(root, text="0", padx=40, pady=40, command=lambda: click(0)).grid(row=4, column=0)
badd= Button(root, text="+", padx=40, pady=40, command=add).grid(row=4, column=1)
bequal= Button(root, text="=", padx=40, pady=40, command=equal).grid(row=4, column=2)
bclear= Button(root, text="AC", padx=40, pady=40, command=clear).grid(row=6, column=0)
bmultiply= Button(root, text="X", padx=40, pady=40, command=multiply).grid(row=5, column=0)
bdivision= Button(root, text="/", padx=40, pady=40, command=division).grid(row=5, column=1)
bsubtraction= Button(root, text="-", padx=40, pady=40, command=subtraction).grid(row=5, column=2)


root.mainloop()