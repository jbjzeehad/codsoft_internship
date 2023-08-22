import tkinter as tk
import tkinter
from tkinter import *


root = Tk()

L1 = Label(root, text="User Name")
L1.grid(row=0, column=0)
L2 = Label(root, text="Password")
L2.grid(row=1, column=0)

mystr = StringVar()
mystr.set('username@xyz.com')

entry = Entry(textvariable=mystr,
              state=DISABLED).grid(row=0,
                                   column=1,
                                   padx=10,
                                   pady=10)

passwd = Entry().grid(row=1, column=1,
                      padx=10, pady=10)
mainloop()


root = tk.Tk()
root.geometry("200x100")

textBox = tk.Entry(root)
textBox.insert(0, "This is the default text")
textBox.pack()
root.mainloop()
