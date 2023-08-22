

# @ Jubayer Bin Jaman | Codsoft


from tkinter import *


def add_cal(num1, num2):
    add_tot = num1 + num2
    return add_tot


def sub_cal(num1, num2):
    sub_tot = num1 - num2
    return sub_tot


def mul_cal(num1, num2):
    mul_tot = num1 * num2
    return mul_tot


def div_cal(num1, num2):
    div_tot = num1 / num2
    return div_tot


# def btn_click(btn):


cal_sc = Tk()
cal_sc.geometry("430x435")
cal_sc.resizable(False, False)
cal_sc.title('Calculator')
cal_sc.iconbitmap(r'F:\codsoft_internship\CODSOFT\task_02\cal_bg.ico')
cal_sc.config(bg='orange')


sc_frm = Frame(cal_sc, width=436, height=90, bd=0, highlightbackground='orange',
               highlightcolor='orange', highlightthickness=1)
sc_frm.pack(side=TOP, pady=2)


sc_fld = Entry(sc_frm, font=('Consolas', 30, 'bold'), borderwidth=1,
               width=20, bg='black', fg='white', bd=0, justify=RIGHT)
sc_fld.grid(row=0, column=0)
sc_fld.pack(ipady=24)


button_frm = Frame(cal_sc, width=436, height=360, bg='orange')
button_frm.pack()

Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='7').grid(row=1, column=0)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='8').grid(row=1, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='9').grid(row=1, column=2)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='/', activebackground='green').grid(row=1, column=3)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='4').grid(row=2, column=0, pady=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='5').grid(row=2, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='6').grid(row=2, column=2)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='X', activebackground='green').grid(row=2, column=3)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='1').grid(row=3, column=0)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='2').grid(row=3, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='3').grid(row=3, column=2)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='-', activebackground='green').grid(row=3, column=3)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='C', activebackground='cyan').grid(row=4, column=0, padx=1, pady=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='0').grid(row=4, column=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='=', activebackground='orange').grid(row=4, column=2, padx=1)
Button(button_frm, background='black', fg='white', width=10, height=3, borderwidth=0,
       text='+', activebackground='green').grid(row=4, column=3)

cal_sc.mainloop()
