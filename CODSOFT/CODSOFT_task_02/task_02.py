

# @ Jubayer Bin Jaman | CodSoft


from tkinter import *

# creating widget,icon,title

cal_sc = Tk()
cal_sc.geometry("430x435")
cal_sc.resizable(False, False)
cal_sc.title('Calculator')
cal_sc.iconbitmap(r'F:\codsoft_internship\CODSOFT\task_02\cal_bg.ico')
cal_sc.config(bg='orange')

# function for the mathematical solution


def button_equal():
    global sc_out
    solution = str(eval(sc_out))  # eval() function for do the math
    btn_in.set(solution)
    sc_out = ""

# function for clear button


def button_clear():
    global sc_out
    sc_out = ""
    btn_in.set("")

# frame for the entry input to show the value


sc_frm = Frame(cal_sc, width=436, height=90, bd=0, highlightbackground='orange',
               highlightcolor='orange', highlightthickness=1)
sc_frm.pack(side=TOP, pady=2)

# for entry function in the frame

sc_out = ""  # default empty screen
btn_in = StringVar()
sc_fld = Entry(sc_frm, textvariable=btn_in, font=('Consolas', 30, 'bold'), borderwidth=1, disabledbackground='black', disabledforeground='white', state=DISABLED,
               width=20, bd=0, justify=RIGHT)
sc_fld.grid(row=0, column=0)
sc_fld.pack(ipady=24)

# frame for the button

button_frm = Frame(cal_sc, width=436, height=360, bg='orange')
button_frm.pack()

# function for when click button


def button_click(btn):
    global sc_out
    sc_out = sc_out + str(btn)
    btn_in.set(sc_out)

# every button and their action


Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='7', command=lambda: [button_click(7)]).grid(row=1, column=0)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='8', command=lambda: [button_click(8)]).grid(row=1, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='9', command=lambda: [button_click(9)]).grid(row=1, column=2)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='/', activebackground='green', command=lambda: [button_click("/")]).grid(row=1, column=3)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='4', command=lambda: [button_click(4)]).grid(row=2, column=0, pady=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='5', command=lambda: [button_click(5)]).grid(row=2, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='6', command=lambda: [button_click(6)]).grid(row=2, column=2)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='X', activebackground='green', command=lambda: [button_click('*')]).grid(row=2, column=3)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='1', command=lambda: [button_click(1)]).grid(row=3, column=0)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='2', command=lambda: [button_click(2)]).grid(row=3, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='3', command=lambda: [button_click(3)]).grid(row=3, column=2)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='-', activebackground='green', command=lambda: [button_click("-")]).grid(row=3, column=3)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='C', activebackground='cyan', command=lambda: [button_clear()]).grid(row=4, column=0, padx=1, pady=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='0', command=lambda: [button_click(0)]).grid(row=4, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='=', activebackground='orange', command=lambda: [button_equal()]).grid(row=4, column=2, padx=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='+', activebackground='green', command=lambda: [button_click("+")]).grid(row=4, column=3)

cal_sc.mainloop()
