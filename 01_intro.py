from tkinter import *


root = Tk()
#creating a label widget
myLabel = Label(root, text = "Hello World")
#pushing it on to the screen
myLabel.pack()

# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying 
root.mainloop()