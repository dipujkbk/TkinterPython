from tkinter import *

root = Tk()
mylabel1 = Label(root,text='Hello World!')
mylabel2 = Label(root,text = 'My name is John Elder!')
mylabel3 = Label(root,text = 'I live in Odisha!').grid(row=1, column=1)

mylabel1.grid(row=0 ,column=0)
mylabel2.grid(row=1, column=5) #actually its realtive


root.mainloop()