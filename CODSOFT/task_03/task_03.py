

# @ Jubayer Bin Jaman | Codsoft


from tkinter import *
import random
import pyperclip


rpg_wid = Tk()
rpg_wid.geometry('366x370')
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
    row=0, column=0, columnspan=3)


Label(rpg_wid, text="PASSWORD", font=('console', 30)).grid(
    row=1, column=0, columnspan=3, pady=20)

Label(rpg_wid, text="Length", font=('verdana', 20)).grid(
    row=2, column=0, columnspan=3, pady=21)


Button(rpg_wid, text='Weak', borderwidth=1,
       width=11, height=2, activebackground='#ff0027').grid(row=3, column=0)
Button(rpg_wid, text='Medium', borderwidth=1, width=11, height=2,
       activebackground='#ffef00').grid(row=3, column=1)
Button(rpg_wid, text='Strong', borderwidth=1, width=11, height=2,
       activebackground='#a2ff00').grid(row=3, column=2)


rpg_wid.mainloop()
