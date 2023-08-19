

# @ Jubayer Bin Jaman | Codsoft


import random
from tkinter import *


def number_generate():
    random_number = random.randint(1, 3)
    return random_number


def check(player, pc):
    if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
        return "YOU WIN"
    if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
        return "PC WIN"
    return "DRAW"


def game():
    print("Rock[1], Paper[2], Scissor[3]: ")
    user = int(input())
    random_number = number_generate()
    if random_number == 1:
        print("PC choose: Rock")
    elif random_number == 2:
        print("PC choose: Paper")
    elif random_number == 3:
        print("PC choose: Scissor")
    decision = check(user, random_number)
    return decision


'''
print("Start[1] | Exit[0]")
choice = int(input())
if choice == 1:
    while True:
        result = game()
        print(result)
        print("Try Again ?? >> YES[1] | NO[0]")
        choice = int(input())
        if choice == 1:
            continue
        else:
            break
print("Thank You")
'''

rps_wind = Tk()
rps_wind.geometry("600x600")
rps_wind.resizable(False, False)
rps_wind.title("RPS Game")
rps_wind.iconbitmap(r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
# rps_wind.config(bg='bg_img')
'''
bg_img = PhotoImage(file=r'F:\codsoft_internship\CODSOFT\task_01\bg.jpg')
label2 = Label(rps_wind, image=bg_img)
label2.place(x=0, y=0)
'''
bk_grnd = PhotoImage(
    file="F:\codsoft_internship\CODSOFT\task_02\rps_logo.png")
label1 = Label(rps_wind, image=bk_grnd)
label1.place(x=0, y=0)
Button(rps_wind, text="strt window",
       command=lambda: [rps_wind.destroy(), exit_wind()]).pack(side=BOTTOM)


def instr_wind():
    print("ok")
    rps_wind = Tk()
    rps_wind.geometry("500x550")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    Button(rps_wind, text="START GAME", command=lambda: [
           rps_wind.destroy(), game_wind()])
    rps_wind.mainloop()


def game_wind():
    rps_wind = Tk()
    rps_wind.geometry("500x550")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    Label(rps_wind, text='pc pic', font=('consolas', 20)).grid(row=0, column=1)
    Label(rps_wind, text='pcr', font=('consolas', 20)).grid(row=1, column=0)
    Label(rps_wind, text='pcw', font=('consolas', 20)).grid(row=1, column=1)
    Label(rps_wind, text='pcp', font=('consolas', 20)).grid(row=1, column=2)
    Label(rps_wind, text='up', font=('consolas', 20)).grid(row=2, column=0)
    Label(rps_wind, text='uw', font=('consolas', 20)).grid(row=2, column=1)
    Label(rps_wind, text='ur', font=('consolas', 20)).grid(row=2, column=2)
    Button(rps_wind, text="TRY AGAIN", command=lambda: [
           rps_wind.destroy(), exit_wind()])

    image1 = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\rock_img.png")
    rock_img = image1.subsample(4, 4)
    Button(rps_wind, text='ROCK', activebackground='green', bd=2, fg='teal', font=('Cooper Black', 15),
           image=rock_img, compound=TOP).grid(row=3, column=0, padx=10)  # button padding from window, side from window

    image2 = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\paper_img.png")
    paper_img = image2.subsample(4, 4)
    Button(rps_wind, bd=2, text='PAPER', activebackground='green', fg='orange', font=('Cooper Black', 15),
           image=paper_img, compound=TOP).grid(row=3, column=1, padx=10)

    image3 = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\scissor_img.png")
    scissor_img = image3.subsample(4, 4)
    Button(rps_wind, bd=2, fg='indigo', activebackground='green', text='SCISSOR', font=('Cooper Black', 15),
           image=scissor_img, compound=TOP).grid(row=3, column=2, padx=10)

    rps_wind.mainloop()


def exit_wind():
    rps_wind = Tk()
    rps_wind.geometry("500x550")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    Button(rps_wind, text="PLAY AGAIN", command=lambda: [
           rps_wind.destroy(), game_wind()]).pack(side=BOTTOM)
    Button(rps_wind, text="EXIT", command=rps_wind.destroy).pack(side=TOP)
    rps_wind.mainloop()


rps_wind.mainloop()
