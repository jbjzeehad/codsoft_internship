
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
cal_sc.geometry("500x700")
cal_sc.resizable(False, False)
cal_sc.title('Calculator')
# cal_sc.iconbitmap(r')

cal_sc_output = Text(cal_sc, width=20, height=3, font=('Consolas', 20))
cal_sc_output.grid(columnspan=5)


cal_sc.mainloop()
