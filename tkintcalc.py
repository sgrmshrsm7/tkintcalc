#!/usr/bin/python

from tkinter import *
import math
result = ''

def add(num):
	global result
	result = result + str(num)
	equation.set(result)

def calculate():
        try:
                global result
                if result != '':
                        result = str(eval(result))
                        if len(result.split('.')) > 1 and result.split('.')[1] == '0':
                                result = result.split('.')[0]
                        equation.set(result)
                else:
                        equation.set('0')
        except:
                equation.set('error')
                result = ''

def floorit():
        calculate()
        global result
        result = result.split('.')[0]
        equation.set(result)
        if len(result) > 1 and result[0] == '-':
                m = '-1'
        else:
                m = ''
        add(m)
        calculate()

def sqrtit():
        calculate()
        global result
        if result != '':
                result = str(math.sqrt(float(result)))
                equation.set(result)

def changesign():
        calculate()
        add('*(-1)')
        calculate()

def back():
        global result
        result = result[:-1]
        equation.set(result)

def clear():
	global result
	result = ''
	equation.set('0')

calc = Tk()
calc.minsize(420, 480)
calc.maxsize(420, 480)
positionRight = int(calc.winfo_screenwidth() / 2 - 250)
positionDown = int(calc.winfo_screenheight() / 2 - 250)
calc.geometry('+{}+{}'.format(positionRight, positionDown))
calc.configure(background='#1a1a1a')
calc.title('tkintcalc')

equation = StringVar()
expression_field = Entry(calc, borderwidth = 0, textvariable = equation, justify = 'right', fg = '#1a1a1a', bg = '#ffffff', font = 'Helvetica 30 bold')
expression_field.place(x = 10, y = 10, height = 50, width = 400)

equation.set('0')
btncolor = '#0080ff'
btntxt = '#ffffff'

button7 = Button(calc, text = ' 7 ', fg = btntxt, bg = btncolor, command = lambda: add(7), font = 'Helvetica 22 bold', borderwidth = 0)
button7.place(x = 10, y = 120, height = 50, width = 92.5)
button8 = Button(calc, text = ' 8 ', fg = btntxt, bg = btncolor, command = lambda: add(8), font = 'Helvetica 22 bold', borderwidth = 0)
button8.place(x = 112.5, y = 120, height = 50, width = 92.5)
button9 = Button(calc, text = ' 9 ', fg = btntxt, bg = btncolor, command = lambda: add(9), font = 'Helvetica 22 bold', borderwidth = 0)
button9.place(x = 215, y = 120, height = 50, width = 92.5)
plus = Button(calc, text = ' + ', fg = btntxt, bg = btncolor, command = lambda: add('+'), font = 'Helvetica 22 bold', borderwidth = 0)
plus.place(x = 317.5, y = 120, height = 50, width = 92.5)

button4 = Button(calc, text = ' 4 ', fg = btntxt, bg = btncolor, command = lambda: add(4), font = 'Helvetica 22 bold', borderwidth = 0)
button4.place(x = 10, y = 180, height = 50, width = 92.5)
button5 = Button(calc, text = ' 5 ', fg = btntxt, bg = btncolor, command = lambda: add(5), font = 'Helvetica 22 bold', borderwidth = 0)
button5.place(x = 112.5, y = 180, height = 50, width = 92.5)
button6 = Button(calc, text = ' 6 ', fg = btntxt, bg = btncolor, command = lambda: add(6), font = 'Helvetica 22 bold', borderwidth = 0)
button6.place(x = 215, y = 180, height = 50, width = 92.5)
minus = Button(calc, text = ' - ', fg = btntxt, bg = btncolor, command = lambda: add('-'), font = 'Helvetica 22 bold', borderwidth = 0)
minus.place(x = 317.5, y = 180, height = 50, width = 92.5)

button1 = Button(calc, text = ' 1 ', fg = btntxt, bg = btncolor, command = lambda: add(1), font = 'Helvetica 22 bold', borderwidth = 0)
button1.place(x = 10, y = 240, height = 50, width = 92.5)
button2 = Button(calc, text = ' 2 ', fg = btntxt, bg = btncolor, command = lambda: add(2), font = 'Helvetica 22 bold', borderwidth = 0)
button2.place(x = 112.5, y = 240, height = 50, width = 92.5)
button3 = Button(calc, text = ' 3 ', fg = btntxt, bg = btncolor, command = lambda: add(3), font = 'Helvetica 22 bold', borderwidth = 0)
button3.place(x = 215, y = 240, height = 50, width = 92.5)
multiply = Button(calc, text = ' * ', fg = btntxt, bg = btncolor, command = lambda: add('*'), font = 'Helvetica 22 bold', borderwidth = 0)
multiply.place(x = 317.5, y = 240, height = 50, width = 92.5)

parenleft = Button(calc, text = ' ( ', fg = btntxt, bg = btncolor, command = lambda: add('('), font = 'Helvetica 22 bold', borderwidth = 0)
parenleft.place(x = 10, y = 300, height = 50, width = 92.5)
button0 = Button(calc, text = ' 0 ', fg = btntxt, bg = btncolor, command = lambda: add(0), font = 'Helvetica 22 bold', borderwidth = 0)
button0.place(x = 112.5, y = 300, height = 50, width = 92.5)
parenright = Button(calc, text = ' ) ', fg = btntxt, bg = btncolor, command = lambda: add(')'), font = 'Helvetica 22 bold', borderwidth = 0)
parenright.place(x = 215, y = 300, height = 50, width = 92.5)
divide = Button(calc, text = ' / ', fg = btntxt, bg = btncolor, command = lambda: add('/'), font = 'Helvetica 22 bold', borderwidth = 0)
divide.place(x = 317.5, y = 300, height = 50, width = 92.5)

floor = Button(calc, text = 'floor', fg = btntxt, bg = btncolor, command = floorit, font = 'Helvetica 22 bold', borderwidth = 0)
floor.place(x = 10, y = 360, height = 50, width = 92.5)
sqrroot= Button(calc, text = 'sqrt', fg = btntxt, bg = btncolor, command = sqrtit, font = 'Helvetica 22 bold', borderwidth = 0)
sqrroot.place(x = 112.5, y = 360, height = 50, width = 92.5)
power = Button(calc, text = ' ^ ', fg = btntxt, bg = btncolor, command = lambda: add('**'), font = 'Helvetica 22 bold', borderwidth = 0)
power.place(x = 215, y = 360, height = 50, width = 92.5)
signchange = Button(calc, text = ' +- ', fg = btntxt, bg = btncolor, command = changesign, font = 'Helvetica 22 bold', borderwidth = 0)
signchange.place(x = 317.5, y = 360, height = 50, width = 92.5)

clear = Button(calc, text = 'CE', fg = btntxt, bg = btncolor, command = clear, font = 'Helvetica 22 bold', borderwidth = 0)
clear.place(x = 10, y = 420, height = 50, width = 92.5)
Decimal= Button(calc, text = '.', fg = btntxt, bg = btncolor, command = lambda: add('.'), font = 'Helvetica 22 bold', borderwidth = 0)
Decimal.place(x = 112.5, y = 420, height = 50, width = 92.5)
backspace = Button(calc, text = ' <-- ', fg = btntxt, bg = btncolor, command = back, font = 'Helvetica 22 bold', borderwidth = 0)
backspace.place(x = 215, y = 420, height = 50, width = 92.5)
equal = Button(calc, text = ' = ', fg = btntxt, bg = btncolor, command = calculate, font = 'Helvetica 22 bold', borderwidth = 0)
equal.place(x = 317.5, y = 420, height = 50, width = 92.5)

calc.mainloop()