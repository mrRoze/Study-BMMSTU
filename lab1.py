import sys
import math
from math import sqrt
from tkinter import *

# создание программы биквадратного уравнения
# изначальные значения
#1 0 -4

def coef(a, b, c):
    D = b*b-4*a*c
    if D >= 0:
        t1 = (-b - sqrt(D))/(2*a)
        t2 = (-b + sqrt(D))/(2*a)
        x1 = sqrt(t1)
        x2 = - sqrt(t1)
        x3 = sqrt(t2)
        x4 = - sqrt(t2)
        text = "Тк это биквадратное уравнение c дискриминантом D = %s, то делая постановку t, получаем слд. корни:\n x1 = %s \n x2= %s \n x3= %s \n x4= %s \n" % (D, x1, x2, x3, x4)
    else:
        text = "Дискриминант равен: %s \n Данное уровнение не имеет место быть" % D
    return text

def inserter(value):
    output.delete("0.0","end")
    output.insert("0.0",value)

def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(coef(a_val, b_val, c_val))
    except ValueError:
        inserter("Комон, введи три (3) числа")

def clear(event):
    caller = event.widget
    caller.delete("0", "end")


root = Tk()

root.title("Биквадратный калькулятор. Фоминский")

root.minsize(325,230)
root.resizable(width=False, height=False)

frame = Frame(root)
frame.grid()

a = Entry(frame, width=3)
a.bind("<FocusIn>", clear)
a.grid(row=1,column=1,padx=(10,0))

a_lab = Label(frame, text="x^4+").grid(row=1,column=2)

b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)

b_lab = Label(frame, text="x^2+").grid(row=1, column=4)

c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)

c_lab = Label(frame, text="= 0").grid(row=1, column=6)

but = Button(frame, text="Решать", command=handler).grid(row=1, column=7, padx=(10,0))
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()