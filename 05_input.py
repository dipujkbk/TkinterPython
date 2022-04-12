from tkinter import *

root = Tk()

e = Entry(root, width = 50,bg='green',fg='yellow',borderwidth=5)
e.pack()
e.insert(0,"Enter Your Name : ") # put some default text inside the box

def myClick():
    mystr = "Hello "+ e.get() # to get the text from the input object
    mylabel = Label(root, text=mystr)
    mylabel.pack()

mybutton1 = Button(root,text = "Enter your Stack Qoute",command= myClick,fg="blue",bg='yellow').pack()

root.mainloop()