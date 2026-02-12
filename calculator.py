# importing
from tkinter import *
from tkinter import ttk

# GUI interaction
window = Tk()
window.title("Calculator")
window.geometry("400x450")

# adding inputs

# ENTRY BOX

e = Entry(window, width= 30, font=('Arial 36'))
e.place(x = 0, y = 0)



# BUTTONS

def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window,text="1",height = 3 ,width=16, command=lambda:click(1))
b.place(x = 10,y = 60)

b = Button(window,text="2",height = 3 ,width=16, command=lambda:click(2))
b.place(x = 140,y = 60)

b = Button(window,text="3",height = 3 ,width=16, command=lambda:click(3))
b.place(x = 270,y = 60)

b = Button(window,text="4",height = 3 ,width=16, command=lambda:click(4))
b.place(x = 10,y = 120)

b = Button(window,text="5",height = 3 ,width=16, command=lambda:click(5))
b.place(x = 140,y = 120)

b = Button(window,text="6",height = 3 ,width=16, command=lambda:click(6))
b.place(x = 270,y = 120)

b = Button(window,text="7",height = 3 ,width=16, command=lambda:click(7))
b.place(x = 10,y = 180)

b = Button(window,text="8",height = 3 ,width=16, command=lambda:click(8))
b.place(x = 140,y = 180)

b = Button(window,text="9",height = 3 ,width=16, command=lambda:click(9))
b.place(x = 270,y = 180)

b = Button(window,text="0",height = 3 ,width=16, command=lambda:click(0))
b.place(x = 10,y = 240)

# OPERATORS
def add():
    n1 = e.get()
    global  math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window,text="+",height = 3 ,width=16, command=add)
b.place(x = 140,y = 240)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window,text="-",height = 3 ,width=16, command = sub)
b.place(x = 270,y = 240)

def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window,text="*",height = 3 ,width=16, command = mul)
b.place(x = 10,y = 300)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window,text="/",height = 3 ,width=16, command = div)
b.place(x = 140,y = 300)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))



b = Button(window,text="=",height = 3 ,width=16, command = equal)
b.place(x = 270,y = 300)

def clear():
    e.delete(0, END)
b = Button(window,text="clear",height = 4 ,width=53, command = clear)
b.place(x = 10,y = 370)
window.mainloop()