from Tkinter import *
import parser

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
        
def openfileR():
    f=open("Readme2.txt", "r")
    f.close()


def openfileW():
    f = open("Readme2.txt", "w")
    f.close()

def generate():
    while(1):
        print "hello"

display = Entry(root)
display.grid(row = 1, columnspan = 6)

button1 = Button(root, text = "1", command = lambda : get_variables(1))
button1.grid(row = 2, column = 0)

button2 = Button(root, text = "2", command = lambda : get_variables(2))
button2.grid(row = 2, column = 1)

button3 = Button(root, text = "3", command = lambda : get_variables(3))
button3.grid(row = 2, column = 2)

button4 = Button(root, text = "4", command = lambda : get_variables(4))
button4.grid(row = 3 , column = 0)

button5 = Button(root, text = "5", command = lambda : get_variables(5))
button5.grid(row = 3, column = 1)

button6 = Button(root, text = "6", command = lambda : get_variables(6))
button6.grid(row = 3, column = 2)

button7 = Button(root, text = "7", command = lambda : get_variables(7))
button7.grid(row = 4, column = 0)

button8 = Button(root, text = "8", command = lambda : get_variables(8))
button8.grid(row = 4, column = 1)

button9 = Button(root , text = "9", command = lambda : get_variables(9))
button9.grid(row = 4, column = 2)

clear = Button(root, text = "AC", command = clear_all)
clear.grid(row = 5, column = 0)

zero = Button(root, text = "0", command = lambda : get_variables(0))
zero.grid(row = 5, column = 1)

result = Button(root, text = "=", command = calculate)
result.grid(row = 3, column = 4, sticky = N+S, rowspan= 15)

plus = Button(root, text = "+", command =  lambda : get_operation("+"))
plus.grid(row = 2, column = 3)

minus = Button(root, text = "-", command =  lambda : get_operation("-"))
minus.grid(row = 3, column = 3)

multiply = Button(root,text = "*", command =  lambda : get_operation("*"))
multiply.grid(row = 4, column = 3)

divide = Button(root, text = "/", command = lambda :  get_operation("/"))
divide.grid(row = 5, column = 3)


percent = Button(root, text = "%", command = lambda :  get_operation("%"))
percent.grid(row = 5, column = 2)


ex = Button(root, text = "^2", command = lambda :  get_operation("**2"))
ex.grid(row = 2, column = 4)


menubar = Menu(root)
filemenu =Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

root.mainloop()