from tkinter import *

root = Tk()

mybutton1 = Button(root,text = "Click Me!",state=DISABLED).pack()
mybutton2 = Button(root,text = "Click here!",padx=50,pady=50).pack()


root.mainloop()