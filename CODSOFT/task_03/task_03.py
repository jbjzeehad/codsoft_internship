

# @ Jubayer Bin Jaman | Codsoft


from tkinter import *
import random
import pyperclip


rpg_wid = Tk()
rpg_wid.geometry('500x500')
rpg_wid.resizable(False, False)
rpg_wid.title('Password Generator')


weak_pass = 'abcdefghijklmnopqrstuvwxyz'
medium_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
strong_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

length_pass = IntVar

# def weak():


Button(rpg_wid, text='Weak').grid(row=3, column=1)
Button(rpg_wid, text='Medium').grid(row=3, column=2)
Button(rpg_wid, text='Strong').grid(row=3, column=3)


rpg_wid.mainloop()
