from Tkinter import * 
import tkMessageBox

totalnumber= ""

def buttonpress():
    entrytxt = entry1.get()
    print entrytxt
    tkMessageBox.showinfo("heres me", entrytxt)
    

def clearlist(event):
    listbox1.delete(0,END)
    
def callback(number):
    global totalnumber
    totalnumber = totalnumber + number
    entry1.insert(END, number)
    print totalnumber

def openfileR():
    f=open("Readme2.txt.", "r")
    for line in f:
        name = line[0:3]
        listbox1.insert(END, name)
    f.close()
    findsize()

def openfileW():
    f = open("Readme2.txt", "w")
    names = listbox1.get(0, END)
    for i in names:
        f.write(i+"\n")
    f.close()

def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

root = Tk()
root.title("Scientific Calculator")

listbox1= (Listbox(root, height=1))
listbox1.grid(row= 7, column= 0 , sticky =EW, columnspan= 8)
listbox1.bind("<Button-3>", clearlist)

button1 = Button(root, text = "1",command=lambda: callback("1"))
button1.grid(row=5, column = 0, columnspan=2)

button2 = Button(root, text = "2", command=lambda: callback("2"))
button2.grid(row=5, column =2, columnspan=2)

button2 = Button(root, text = "3", command=lambda: callback("3"))
button2.grid(row=5, column =4, columnspan=2)

button2 = Button(root, text = "4", command=lambda: callback("4"))
button2.grid(row=4, column = 0, columnspan=2)


button2 = Button(root, text = "5", command=lambda: callback("5"))
button2.grid(row=4, column = 2, columnspan=2)

button2 = Button(root, text = "6", command=lambda: callback("6"))
button2.grid(row=4, column = 4, columnspan=2)

button2 = Button(root, text = "7", command=lambda: callback("7"))
button2.grid(row=3, column = 0, columnspan=2)

button2 = Button(root, text = "8", command=lambda: callback("8"))
button2.grid(row=3, column = 2, columnspan=2)

button2 = Button(root, text = "9", command=lambda: callback("9"))
button2.grid(row=3, column = 4, columnspan=2)


button2 = Button(root, text = "-", command=lambda: callback("-"))
button2.grid(row=4, column = 6, columnspan=2)

button2 = Button(root, text = "0", command=lambda: callback("0"))
button2.grid(row=6, column = 0, columnspan=2)

button2 = Button(root, text = "+", command=lambda: callback("+"))
button2.grid(row=3, column = 6, columnspan=2)

button2 = Button(root, text = ".", command=lambda: callback("."))
button2.grid(row=6, column = 2, columnspan=2)

button1 = Button(root, text = "=", command=lambda: callback("="))
button1.grid(row=6, column=4, columnspan=2)

button2 = Button(root, text = "/", command=lambda: callback("/"))
button2.grid(row=6, column = 6, columnspan=2)

button2 = Button(root, text = "*", command=lambda: callback("*"))
button2.grid(row=5, column = 6, columnspan=2)

button2 = Button(root, text = "-", command=lambda: callback("-"))
button2.grid(row=4, column = 6, columnspan=2)

entry1 = Entry(root)
entry1.grid(row=1, column=0,columnspan=8)
entry1.bind("<Return>")

#label1 = Label(root, text = "Best calculator ever", bg="purple", anchor=W, )
#label1.grid(row=0, column=0, sticky=EW, columnspan=8)




menubar = Menu(root)
filemenu =Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=openfileW)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)

mainloop() #causes the windows to display on the screen until program closes