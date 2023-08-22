

# @ Jubayer Bin Jaman | Codsoft


from tkinter import *
import random

# creating widget,size,icon,title

rpg_wid = Tk()
rpg_wid.geometry('366x330')
rpg_wid.resizable(False, False)
rpg_wid.title('Password Generator')
rpg_wid.iconbitmap(r'F:\codsoft_internship\CODSOFT\task_03\rpg.ico')
rpg_wid.config(bg='white')

# for weak password


def weak():
    length = int(length_pass.get())
    final_pass = ""
    weak_pass = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0, length):
        final_pass = final_pass + random.choice(weak_pass)
    password = StringVar()
    password.set(final_pass)  # for showing pass on screen
    Entry(
        rpg_wid, textvariable=password, font=('console', 13, 'bold'), justify=CENTER, width=39, disabledbackground='white', borderwidth=0, state=DISABLED).grid(row=1, column=0, columnspan=3, pady=10)

# for meium password


def medium():
    length = int(length_pass.get())
    final_pass = ""
    medium_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in range(0, length):
        final_pass = final_pass + random.choice(medium_pass)
    password = StringVar()  # for showing pass on screen
    password.set(final_pass)
    Entry(
        rpg_wid, textvariable=password, font=('console', 13, 'bold'), justify=CENTER, width=39, disabledbackground='white', borderwidth=0, state=DISABLED).grid(row=1, column=0, columnspan=3, pady=10)

# for strong password


def strong():
    length = int(length_pass.get())
    final_pass = ""
    strong_pass = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    for i in range(0, length):
        final_pass = final_pass + random.choice(strong_pass)
    password = StringVar()
    password.set(final_pass)  # for showing pass on screen
    Entry(
        rpg_wid, textvariable=password, font=('console', 13, 'bold'), justify=CENTER, width=39, disabledbackground='white', borderwidth=0, state=DISABLED).grid(row=1, column=0,  columnspan=3, pady=10)

# for input pasword length


length_pass = StringVar()
length_pass_entry = Entry(
    rpg_wid, textvariable=length_pass, font=('verdana', 20), justify=CENTER, borderwidth=1).grid(row=2, column=0, columnspan=3, pady=12)

# image on the top

top_img = PhotoImage(file="F:\codsoft_internship\CODSOFT\\task_03\\rpg_bg.png")
top_bg_img = top_img.subsample(3, 3)
Label(rpg_wid, image=top_bg_img).grid(
    row=0, column=0, columnspan=3)

# label for the first time on the screen

pass_label = Label(rpg_wid, text="PASSWORD",
                   background="white", font=('console', 30))
pass_label.grid(
    row=1, column=0, columnspan=3, pady=10)

# for removing the label


def remove():
    pass_label.config(text="")

# creating button for weak password genarate


Button(rpg_wid, text='Weak', borderwidth=1,
       width=11, height=2, command=lambda: [remove(), weak()]).grid(row=3, column=0)

# creating button for medium password genarate

Button(rpg_wid, text='Medium', borderwidth=1, width=11, height=2,
       command=lambda: [remove(), medium()]).grid(row=3, column=1)

# creating button for strong password genarate

Button(rpg_wid, text='Strong', borderwidth=1, width=11, height=2,
       command=lambda: [remove(), strong()]).grid(row=3, column=2)

rpg_wid.mainloop()
