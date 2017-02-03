# -*- coding: utf-8 -*-

from Tkinter import *
import parser
import Tkinter
import tkFileDialog

root = Tk()
root.title('Calculator')

i = 0

def clear_all():
    display.delete(0, END)

def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    whole_string = display.get()
    if len(whole_string):        
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")
        
    
def file_save():
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: 
        return
    text2save = str(text.get(1.0, END)) 
    f.write(text2save)
    f.close() 
    
def file_open():
    f = tkFileDialog.askopenfile(mode='r', defaultextension=".txt")
    if f is None: 
        return
    text2save = str(text.get(1.0, END)) 
    f.close() 

def save(self):
    text_box= self.toal
    print text_box
    f= open ("ReadMe.txt.", "w")
    total =str(text_box)
    f.write(total)
    f.close()
    
def askopenfile(self):
    return tkFileDialog.askopenfile(mode='r', **self.file_opt)

text=Text(root)

display = Entry(root)
display.grid(row = 1, columnspan = 6)

button1 = Button(root, text = "1", command = lambda : get_variables(1), foreground ="goldenrod3")
button1.grid(row = 2, column = 0)

button2 = Button(root, text = "2", command = lambda : get_variables(2), foreground ="goldenrod3")
button2.grid(row = 2, column = 1)

button3 = Button(root, text = "3", command = lambda : get_variables(3), foreground ="goldenrod3")
button3.grid(row = 2, column = 2)

button4 = Button(root, text = "4", command = lambda : get_variables(4), foreground ="goldenrod3")
button4.grid(row = 3 , column = 0)

button5 = Button(root, text = "5", command = lambda : get_variables(5), foreground ="goldenrod3")
button5.grid(row = 3, column = 1)

button6 = Button(root, text = "6", command = lambda : get_variables(6), foreground ="goldenrod3")
button6.grid(row = 3, column = 2)

button7 = Button(root, text = "7", command = lambda : get_variables(7), foreground ="goldenrod3")
button7.grid(row = 4, column = 0)

button8 = Button(root, text = "8", command = lambda : get_variables(8), foreground ="goldenrod3")
button8.grid(row = 4, column = 1)

button9 = Button(root , text = "9", command = lambda : get_variables(9), foreground ="goldenrod3")
button9.grid(row = 4, column = 2)

clear = Button(root, text = "AC", command = clear_all)
clear.grid(row = 5, column = 0)

zero = Button(root, text = "0", command = lambda : get_variables(0), foreground ="goldenrod3")
zero.grid(row = 5, column = 1)

result = Button(root, text = "=", command = calculate, foreground = "seagreen")
result.grid(row = 3, column = 4, sticky = N+S, rowspan= 15)

plus = Button(root, text = "+", command =  lambda : get_operation("+"), foreground ="red")
plus.grid(row = 2, column = 3)

minus = Button(root, text = "-", command =  lambda : get_operation("-"), foreground ="red")
minus.grid(row = 3, column = 3)

multiply = Button(root,text = "*", command =  lambda : get_operation("*"), foreground ="red")
multiply.grid(row = 4, column = 3)

divide = Button(root, text = "/", command = lambda :  get_operation("/"), foreground ="red")
divide.grid(row = 5, column = 3)


percent = Button(root, text = "%", command = lambda :  get_operation("%"))
percent.grid(row = 5, column = 2)


eh = Button(root, text = "^2", command = lambda :  get_operation("**2"))
eh.grid(row = 2, column = 4)




menubar = Menu(root)
filemenu =Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=file_open)
filemenu.add_separator()
filemenu.add_command(label="Save", command=file_save)
menubar.add_cascade(label="File", menu=filemenu)

editmenu=Menu(menubar,tearoff=0)

root.config(menu=menubar)

root.mainloop()