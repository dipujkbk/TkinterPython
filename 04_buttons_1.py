from tkinter import *

root = Tk()

def myClick():
    mylabel = Label(root, text='hey, look you clicked a button!')
    mylabel.pack()

mybutton1 = Button(root,text = "Click Me!",command= myClick,fg="blue",bg='yellow').pack()

root.mainloop()