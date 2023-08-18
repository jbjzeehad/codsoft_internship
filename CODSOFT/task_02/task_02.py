
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


cal_sc = Tk()
cal_sc.geometry("440x450")
cal_sc.resizable(False, False)
cal_sc.title('Calculator')
cal_sc.iconbitmap(r'F:\codsoft_internship\CODSOFT\task_02\cal_bg.ico')
cal_sc.config(bg='orange')

cal_sc_output = Text(cal_sc, background='black', fg='white', width=29, height=3,
                     borderwidth=1, font=('Consolas', 20))
cal_sc_output.grid(row=0, column=0, columnspan=4, padx=1, pady=2)


Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='7').grid(row=1, column=0)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='8').grid(row=1, column=1, pady=1)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='9').grid(row=1, column=2)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='/').grid(row=1, column=3)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='4').grid(row=2, column=0)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='5').grid(row=2, column=1, pady=1)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='6').grid(row=2, column=2)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='X').grid(row=2, column=3)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='1').grid(row=3, column=0)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='2').grid(row=3, column=1, pady=1)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='3').grid(row=3, column=2)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='-').grid(row=3, column=3)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='C').grid(row=4, column=0)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='0').grid(row=4, column=1, pady=1)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='=').grid(row=4, column=2)
Button(cal_sc, background='black', fg='white', width=10, height=3, borderwidth=1,
       text='+').grid(row=4, column=3)

cal_sc.mainloop()
