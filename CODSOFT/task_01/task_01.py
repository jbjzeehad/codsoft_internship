

# @ Jubayer Bin Jaman | Codsoft


import random
from tkinter import *


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
rps_wind.geometry("370x400")
rps_wind.resizable(False, False)
rps_wind.title("RPS Game")
rps_wind.iconbitmap(r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
rps_wind.config(bg='#f9f7f0')

bk_grnd = PhotoImage(
    file="F:\codsoft_internship\CODSOFT\\task_01\\rps_logo.png").subsample(2, 2)
label1 = Label(rps_wind, image=bk_grnd, background='#f9f7f0')

label1.place(x=30, y=0)

start_img = PhotoImage(
    file=r"F:\codsoft_internship\CODSOFT\task_01\start_btn.png")
start_btn_img = start_img.subsample(4, 4)
Button(rps_wind, font=('Verdana', 20), borderwidth=0, image=start_btn_img, compound=TOP, background='#f9f7f0', activebackground='#f9f7f0',
       command=lambda: [rps_wind.destroy(), exit_wind()]).pack(side=BOTTOM, pady=50)


def instr_wind():
    print("ok")
    rps_wind = Tk()
    rps_wind.geometry("370x400")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    rps_wind.config('white')
    Button(rps_wind, text="START GAME", command=lambda: [
           rps_wind.destroy(), game_wind()])
    rps_wind.mainloop()


def game_wind():
    rps_wind = Tk()
    rps_wind.geometry("370x400")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    rps_wind.config(bg='#f9f7f0')
#    bk_grnd = PhotoImage(
#        file="F:\codsoft_internship\CODSOFT\\task_01\\rps_logo.png")
#    label1 = Label(rps_wind, image=bk_grnd)
#    label1.place(x=0, y=-50)

    def number_generate():
        random_number = random.randint(1, 3)
        return random_number

    def check(player, pc):

        if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):

            u_win = StringVar()
            u_win.set("WIN")
            Entry(rps_wind, justify=CENTER, textvariable=u_win, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=0)
            pc_loss = StringVar()
            pc_loss.set("LOSS")
            Entry(rps_wind, justify=CENTER, textvariable=pc_loss, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=2)

            return print("YOU WIN")

        if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
            pc_win = StringVar()
            pc_win.set("WIN")
            Entry(rps_wind, justify=CENTER, textvariable=pc_win, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=2)
            u_loss = StringVar()
            u_loss.set("LOSS")
            Entry(rps_wind, justify=CENTER, textvariable=u_loss, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=0)

            return print("PC WIN")
        if (player == pc):
            pc_draw = StringVar()
            pc_draw.set("DRAW")
            Entry(rps_wind, justify=CENTER, textvariable=pc_draw, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=2)
            u_draw = StringVar()
            u_draw.set("DRAW")
            Entry(rps_wind, justify=CENTER, textvariable=u_draw, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=0)

        return print("DRAW")

    def game():
        global player
#        print("Rock[1], Paper[2], Scissor[3]: ")
#        user = int(input())
        random_number = number_generate()
        if random_number == 1:
            print("PC choose: Rock")
            rk_image = PhotoImage(
                file="F:\codsoft_internship\CODSOFT\\task_01\pc_rock_img.png")
            rk_img = rk_image.subsample(4, 4)
            lbl = Label(rps_wind, image=rk_img, background='#f9f7f0')
            lbl.grid(row=1, column=1)

        elif random_number == 2:
            print("PC choose: Paper")
            pr_image = PhotoImage(
                file="F:\codsoft_internship\CODSOFT\\task_01\pc_paper_img.png")
            pr_img = pr_image.subsample(4, 4)
            lbl = Label(rps_wind, image=pr_img, background='#f9f7f0')
            lbl.grid(row=1, column=1)

        elif random_number == 3:
            print("PC choose: Scissor")
            sr_image = PhotoImage(
                file="F:\codsoft_internship\CODSOFT\\task_01\\pc_scissor_img.png")
            sr_img = sr_image.subsample(4, 4)
            lbl = Label(rps_wind, image=sr_img, background='#f9f7f0')
            lbl.grid(row=1, column=1)
        decision = check(player, random_number)
        rps_wind.mainloop()
#        return decision

    user_image = PhotoImage(
        file="F:\codsoft_internship\CODSOFT\\task_01\\rock_img.png")
    user_game_img = user_image.subsample(4, 4)
    user_gm_lbl = Label(rps_wind, image=user_game_img, background="#f9f7f0")
    user_gm_lbl.grid(row=2, column=1, padx=5, pady=10)

    pc_image = PhotoImage(
        file="F:\codsoft_internship\CODSOFT\\task_01\\pc_rock_img.png")
    pc_game_img = pc_image.subsample(4, 4)
    pc_gm_lbl = Label(rps_wind, image=pc_game_img, background="#f9f7f0")
    pc_gm_lbl.grid(row=1, column=1, padx=5, pady=10)

    top_label = Label(rps_wind, justify=CENTER, text='05 POINTS TO WIN', background="#f9f7f0", fg="#72cc50", font=(
        'consolas', 20, 'bold'), width=20).grid(row=0, column=0, columnspan=3)

    u_sc = Entry(rps_wind, justify=CENTER, text='yourscore', font=(
        'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=2)
    pc_sc = Entry(rps_wind, justify=CENTER, text='pcscore', font=(
        'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=0)

    def rock_show():
        global player
        player = 1
        rk_image = PhotoImage(
            file="F:\codsoft_internship\CODSOFT\\task_01\\rock_img.png")
        rk_img = rk_image.subsample(4, 4)
        lbl = Label(rps_wind, image=rk_img, background='#f9f7f0')
        lbl.grid(row=2, column=1)
        game()
        rps_wind.mainloop()

    def paper_show():
        global player
        player = 2
        pr_image = PhotoImage(
            file="F:\codsoft_internship\CODSOFT\\task_01\\paper_img.png")
        pr_img = pr_image.subsample(4, 4)
        lbl = Label(rps_wind, image=pr_img, background='#f9f7f0')
        lbl.grid(row=2, column=1)
        game()
        rps_wind.mainloop()

    def scissor_show():
        global player
        player = 3
        sr_image = PhotoImage(
            file="F:\codsoft_internship\CODSOFT\\task_01\\scissor_img.png")
        sr_img = sr_image.subsample(4, 4)
        lbl = Label(rps_wind, image=sr_img, background='#f9f7f0')
        lbl.grid(row=2, column=1)
        game()
        rps_wind.mainloop()

    Button(rps_wind, text="TRY AGAIN", command=lambda: [
           rps_wind.destroy(), exit_wind()])

    Button(rps_wind, text='ROCK', activebackground='#f9f7f0', background='#f9f7f0', bd=0, fg='#002c3e', activeforeground='#f27777', width=7, height=2, font=('Cooper Black', 15), command=lambda: [rock_show()]
           ).grid(row=3, column=0, padx=5)  # button padding from window, side from window

    Button(rps_wind, text='PAPER', activebackground='#f9f7f0', background='#f9f7f0', bd=0, fg='#002c3e', activeforeground='#f27777',
           width=7, height=2, font=('Cooper Black', 15), command=lambda: [paper_show()]).grid(row=3, column=1)

    Button(rps_wind, text='SCISSOR', activebackground='#f9f7f0', background='#f9f7f0', bd=0, fg='#002c3e', activeforeground='#f27777',
           width=7, height=2, font=('Cooper Black', 15), command=lambda: [scissor_show()]).grid(row=3, column=2, padx=5)

    rps_wind.mainloop()

#####################################################


def exit_wind():
    rps_wind = Tk()
    rps_wind.geometry("370x400")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    retry_img = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\retry_btn.png")
    retry_btn_img = retry_img.subsample(4, 4)
    Button(rps_wind, image=retry_btn_img, borderwidth=0, compound=TOP,
           command=lambda: [rps_wind.destroy(), game_wind()]).pack(side=TOP, pady=80)

    exit_img = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\exit_btn.png")
    exit_btn_img = exit_img.subsample(3, 3)
    Button(rps_wind, image=exit_btn_img, borderwidth=1, compound=TOP,
           command=lambda: [rps_wind.destroy(), game_wind()]).pack(side=BOTTOM, pady=80)
    rps_wind.mainloop()


rps_wind.mainloop()
