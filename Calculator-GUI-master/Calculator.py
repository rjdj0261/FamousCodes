#import modules
import cmath
import tkinter

#def func
expression = ""

#def erasefunc():
def press(num):
    global expression
    expression = expression + (str(num))
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
    except:
        equation.set("error")
        expression = ""

def binary():
    try:
        global expression
        total = str(bin(expression))
        equation.set(total)
    except:
        equation.set("error")
        expression = ""

def hexadecimalfunc():
    try:
        global expression
        total = str(hex(expression))
        equation.set(total)
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def erase():
    txt=equation.get()[:-1]
    equation.set(txt)

#make window
if tkinter._name_ == "_main_":
    gui = tkinter.Tk()
    gui.configure(background="Gray")
    gui.title("Advanced Calculator")

#make expression screen
    equation = tkinter.StringVar()
    expression_field = tkinter.Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=10, ipadx=160, ipady=7)
    equation.set('Enter Your Expression')

#make tkinter.Buttons
tkinter.Button1 = tkinter.Button(gui, text='1', fg='white', bg='Black', command=lambda: press(1), height=3, width=7)

tkinter.Button2 = tkinter.Button(gui, text='2', fg='white', bg='black', command=lambda: press(2), height=3, width=7)

tkinter.Button3 = tkinter.Button(gui, text='3', fg='white', bg='black', command=lambda: press(3), height=3, width=7)

tkinter.Button4 = tkinter.Button(gui, text='4', fg='white', bg='black', command=lambda: press(4), height=3, width=7)

tkinter.Button5 = tkinter.Button(gui, text='5', fg='white', bg='black', command=lambda: press(5), height=3, width=7)

tkinter.Button6 = tkinter.Button(gui, text='6', fg='white', bg='black', command=lambda: press(6), height=3, width=7)

tkinter.Button7 = tkinter.Button(gui, text='7', fg='white', bg='black', command=lambda: press(7), height=3, width=7)

tkinter.Button8 = tkinter.Button(gui, text='8', fg='white', bg='black', command=lambda: press(8), height=3, width=7)

tkinter.Button9 = tkinter.Button(gui, text='9', fg='white', bg='black', command=lambda: press(9), height=3, width=7)

tkinter.Button0 = tkinter.Button(gui, text='0', fg='white', bg='black', command=lambda: press(0), height=3, width=7)

plus = tkinter.Button(gui, text='+', fg='white', bg='black', command=lambda: press("+"), height=3, width=7)

minus = tkinter.Button(gui, text='-', fg='white', bg='black', command=lambda: press("-"), height=3, width=7)

multiply = tkinter.Button(gui, text='*', fg='white', bg='black', command=lambda: press("*"), height=3, width=7)

divide = tkinter.Button(gui, text='/', fg='white', bg='black', command=lambda: press("/"), height=3, width=7)

equal = tkinter.Button(gui, text='=', fg='white', bg='black', command=equalpress, height=3, width=7)

clear = tkinter.Button(gui, text='Clear', fg='white', bg='black', command=clear, height=3, width=7)

Decimal = tkinter.Button(gui, text='.', fg='white', bg='black', command=lambda: press('.'), height=3, width=7)

modulus = tkinter.Button(gui, text='%', fg='white', bg='black', command=lambda: press('%'), height=3, width=7)

power = tkinter.Button(gui, text='**', fg='white', bg='black', command=lambda: press('**'), height=3, width=7)

RoundOfDiv = tkinter.Button(gui, text='//', fg='white', bg='black', command=lambda: press('//'), height=3, width=7)

bracket1 = tkinter.Button(gui, text=('('), fg='white', bg='black', command=lambda: press('('), height=3, width=7)

bracket2 = tkinter.Button(gui, text=')', fg='white', bg='black', command=lambda: press(')'), height=3, width=7)

bracket3 = tkinter.Button(gui, text='[', fg='white', bg='black', command=lambda: press('['), height=3, width=7)

bracket4 = tkinter.Button(gui, text=']', fg='white', bg='black', command=lambda: press(']'), height=3, width=7)

bracket5 = tkinter.Button(gui, text='{', fg='white', bg='black', command=lambda: press('{'), height=3, width=7)

bracket6 = tkinter.Button(gui, text='}', fg='white', bg='black', command=lambda: press('}'), height=3, width=7)

pi = tkinter.Button(gui, text='π', fg='white', bg='black', command=lambda: press(str(cmath.pi)), height=3, width=7)

e = tkinter.Button(gui, text='e', fg='white', bg='black', command=lambda: press(str(cmath.e)), height=3, width=7)

tau = tkinter.Button(gui, text='tau', fg='white', bg='black', command=lambda: press(str(cmath.tau)), height=3, width=7)

nan = tkinter.Button(gui, text='nan', fg='white', bg='black', command=lambda: press(str(cmath.nan)), height=3, width=7)

inf = tkinter.Button(gui, text='inf', fg='white', bg='black', command=lambda: press(str(cmath.inf)), height=3, width=7)

binary1 = tkinter.Button(gui, text='bin', fg='white', bg='black', command=binary, height=3, width=7)

hexadecimal = tkinter.Button(gui, text='hex', fg='white', bg='black', command=hexadecimalfunc, height=3, width=7)

infj = tkinter.Button(gui, text='infj', fg='white', bg='black', command=lambda: press(str(cmath.infj)), height=3, width=7)

nanj = tkinter.Button(gui, text='nanj', fg='white', bg='black', command=lambda: press(str(cmath.nanj)), height=3, width=7)


erase = tkinter.Button(gui, text='<-', fg='white', bg='black', command=erase, height=3, width=7)

#place tkinter.Buttons
tkinter.Button1.grid(row=2, column=0)

tkinter.Button2.grid(row=2, column=1)

tkinter.Button3.grid(row=2, column=2)

tkinter.Button4.grid(row=3, column=0)

tkinter.Button5.grid(row=3, column=1)

tkinter.Button6.grid(row=3, column=2)

tkinter.Button7.grid(row=4, column=0)

tkinter.Button8.grid(row=4, column=1)

tkinter.Button9.grid(row=4, column=2)

tkinter.Button0.grid(row=5, column=2)

plus.grid(row=2, column=3)

minus.grid(row=3, column=3)

multiply.grid(row=4, column=3)

divide.grid(row=5, column=3)

equal.grid(row=5, column=0)

clear.grid(row=5, column=1)

Decimal.grid(row=2, column=4)

modulus.grid(row=3, column=4)

power.grid(row=4, column=4)

RoundOfDiv.grid(row=5, column=4)

bracket1.grid(row=6, column=0)

bracket2.grid(row=6, column=1)

bracket3.grid(row=6, column=2)

bracket4.grid(row=6, column=3)

bracket5.grid(row=7, column=0)

bracket6.grid(row=7, column=1)

pi.grid(row=7, column=2)

e.grid(row=7, column=3)

tau.grid(row=2, column=5)

nan.grid(row=3, column=5)

inf.grid(row=4, column=5)

binary1.grid(row=7, column=4)

hexadecimal.grid(row=6, column=4)

nanj.grid(row=5, column=5)

infj.grid(row=6, column=5)

erase.grid(row=7, column=5)

#mainloop
gui.mainloop()