

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
rps_wind.geometry("900x550")
rps_wind.resizable(False, False)
rps_wind.title("RPS Game")
rps_wind.iconbitmap(r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")

strt_wind = Frame(rps_wind)
game_wind = Frame(rps_wind)


image1 = PhotoImage(file=r"F:\codsoft_internship\CODSOFT\task_01\rock_img.png")
rock_img = image1.subsample(3, 3)
Button(rps_wind, text='ROCK', activebackground='green', bd=2, fg='teal', font=('Cooper Black', 20), image=rock_img, compound=TOP).pack(
    side=LEFT, ipadx=100, padx=10)  # button padding from window, side from window

image2 = PhotoImage(
    file=r"F:\codsoft_internship\CODSOFT\task_01\paper_img.png")
paper_img = image2.subsample(3, 3)
Button(rps_wind, bd=2, text='PAPER', activebackground='green', fg='orange', font=('Cooper Black', 20),
       image=paper_img, compound=TOP).pack(side=LEFT, padx=10)


image3 = PhotoImage(
    file=r"F:\codsoft_internship\CODSOFT\task_01\scissor_img.png")
scissor_img = image3.subsample(3, 3)
Button(rps_wind, bd=2, fg='indigo', activebackground='green', text='SCISSOR', font=('Cooper Black', 20),
       image=scissor_img, compound=TOP).pack(side=LEFT, padx=10)


rps_wind.mainloop()
