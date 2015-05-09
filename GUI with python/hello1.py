from tkinter import *

def buttonPushed():
    print("Button Pushed")
root = Tk()

w = Label(root,text="Hello World")

w.pack()

myButton = Button(root, text="Exit",command=buttonPushed)
myButton.pack()

root.mainloop()

