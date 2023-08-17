
from tkinter import *

cal_sc = Tk()
cal_sc.geometry("500x700")
cal_sc.resizable(False, False)
cal_sc.title('Calculator')
# cal_sc.iconbitmap(r')

cal_sc_output = Text(cal_sc, width=20, height=3, font=('Consolas', 20))
cal_sc_output.grid(columnspan=5)


cal_sc.mainloop()
