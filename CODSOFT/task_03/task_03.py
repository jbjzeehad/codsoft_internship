

# @ Jubayer Bin Jaman | Codsoft


from tkinter import *
import random
import pyperclip


rpg_wid = Tk()
rpg_wid.geometry('366x370')
rpg_wid.resizable(False, False)
rpg_wid.title('Password Generator')
rpg_wid.iconbitmap(r'F:\codsoft_internship\CODSOFT\task_03\rpg.ico')


def weak():
    length = int(length_pass.get())
    final_pass = ""
    weak_pass = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, length):
        final_pass = final_pass + random.choice(weak_pass)
    Label(rpg_wid, text=final_pass, font=('console', 13)).grid(
        row=1, column=0, columnspan=3, pady=15)


def medium():
    length = int(length_pass.get())
    final_pass = ""
    medium_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(0, length):
        final_pass = final_pass + random.choice(medium_pass)
    Label(rpg_wid, text=final_pass, font=('console', 13)).grid(
        row=1, column=0, columnspan=3, pady=15)


def strong():
    length = int(length_pass.get())
    final_pass = ""
    strong_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    for i in range(0, length):
        final_pass = final_pass + random.choice(strong_pass)
    Label(rpg_wid, text=final_pass, font=('console', 13)).grid(
        row=1, column=0, columnspan=3, pady=15)


length_pass = StringVar()
length_pass_entry = Entry(
    rpg_wid, textvariable=length_pass, font=('verdana', 20), justify=CENTER, borderwidth=0).grid(row=2, column=0, columnspan=3, pady=21)

top_img = PhotoImage(file="F:\codsoft_internship\CODSOFT\\task_03\\rpg_bg.png")
top_bg_img = top_img.subsample(3, 3)
Label(rpg_wid, image=top_bg_img).grid(
    row=0, column=0, columnspan=3)

pass_label = Label(rpg_wid, text="PASSWORD", font=('console', 30))
pass_label.grid(
    row=1, column=0, columnspan=3, pady=15)


def remove():
    pass_label.config(text="")


Button(rpg_wid, text='Weak', borderwidth=1,
       width=11, height=2, activebackground='#ff0027', command=lambda: [remove(), weak()]).grid(row=3, column=0)
Button(rpg_wid, text='Medium', borderwidth=1, width=11, height=2,
       activebackground='#ffef00', command=lambda: [remove(), medium()]).grid(row=3, column=1)
Button(rpg_wid, text='Strong', borderwidth=1, width=11, height=2,
       activebackground='#a2ff00', command=lambda: [remove(), strong()]).grid(row=3, column=2)

rpg_wid.mainloop()
