

# @ Jubayer Bin Jaman | Codsoft


from tkinter import *
import random
import pyperclip


rpg_wid = Tk()
rpg_wid.geometry('385x385')
rpg_wid.resizable(False, False)
rpg_wid.title('Password Generator')
rpg_wid.iconbitmap(r'F:\codsoft_internship\CODSOFT\task_03\rpg.ico')


weak_pass = 'abcdefghijklmnopqrstuvwxyz'
medium_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
strong_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

length_pass = IntVar

# def weak():


top_img = PhotoImage(file="F:\codsoft_internship\CODSOFT\\task_03\\rpg_bg.png")
top_bg_img = top_img.subsample(3, 3)
Label(rpg_wid, image=top_bg_img).grid(
    row=0, column=0, columnspan=4)
Button(rpg_wid, text='Weak').grid(row=3, column=1)
Button(rpg_wid, text='Medium').grid(row=3, column=2)
Button(rpg_wid, text='Strong').grid(row=3, column=3)


rpg_wid.mainloop()
