

# @ Jubayer Bin Jaman | Codsoft


import random
from tkinter import *

# start game

rps_wind = Tk()
rps_wind.geometry("370x400")
rps_wind.resizable(False, False)
rps_wind.title("RPS Game")
rps_wind.iconbitmap(r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
rps_wind.config(bg='#f9f7f0')

# addding bkgrnd image

bk_grnd = PhotoImage(
    file="F:\codsoft_internship\CODSOFT\\task_01\\rps_logo.png").subsample(2, 2)
label1 = Label(rps_wind, image=bk_grnd, background='#f9f7f0')
label1.place(x=30, y=0)

# start button

start_img = PhotoImage(
    file=r"F:\codsoft_internship\CODSOFT\task_01\start_btn.png")
start_btn_img = start_img.subsample(4, 4)
Button(rps_wind, font=('Verdana', 20), borderwidth=0, image=start_btn_img, compound=TOP, background='#f9f7f0', activebackground='#f9f7f0',
       command=lambda: [rps_wind.destroy(), game_wind()]).pack(side=BOTTOM, pady=50)

# enter the game


def game_wind():
    rps_wind = Tk()
    rps_wind.geometry("370x400")
    rps_wind.resizable(False, False)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    rps_wind.config(bg='#f9f7f0')

# game screen

    global u_score
    u_score = IntVar()
    u_score = 0
    global pc_score
    pc_score = IntVar()
    pc_score = 0

# variable for score part

    def number_generate():
        random_number = random.randint(1, 3)
        return random_number

# random number for pc's turn

    def check(player, pc):
        global u_score
        global pc_score
# checking who win or loss
        if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):

            u_win = StringVar()
            u_win.set("WIN")
            Entry(rps_wind, justify=CENTER, textvariable=u_win, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=0)
            pc_loss = StringVar()
            pc_loss.set("LOSS")
            Entry(rps_wind, justify=CENTER, textvariable=pc_loss, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=2)
            u_sc = IntVar()
            u_score = u_score + 1
            u_sc.set(u_score)
            Entry(rps_wind, justify=CENTER, textvariable=u_sc, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=2)

# showing useers score and win_loss msg

        if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
            pc_win = StringVar()
            pc_win.set("WIN")
            Entry(rps_wind, justify=CENTER, textvariable=pc_win, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=2)
            u_loss = StringVar()
            u_loss.set("LOSS")
            Entry(rps_wind, justify=CENTER, textvariable=u_loss, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=0)
            pc_sc = IntVar()
            pc_score = pc_score+1
            pc_sc.set(pc_score)
            Entry(rps_wind, justify=CENTER, textvariable=pc_sc, font=('consolas', 20), width=4,
                  borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=0)

# showing pc's score and win_loss msg

        if (player == pc):
            pc_draw = StringVar()
            pc_draw.set("DRAW")
            Entry(rps_wind, justify=CENTER, textvariable=pc_draw, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=1, column=2)
            u_draw = StringVar()
            u_draw.set("DRAW")
            Entry(rps_wind, justify=CENTER, textvariable=u_draw, font=(
                'consolas', 20), width=4, borderwidth=0, state=DISABLED, disabledbackground="#f9f7f0").grid(row=2, column=0)

# for draw

        if u_score == 5 or pc_score == 5:
            if u_score == 5:
                rps_wind.destroy()
                msg = "YOU WIN"
                return exit_wind(msg)
            else:
                rps_wind.destroy()
                msg = "PC WIN"
                return exit_wind(msg)

# when round ends exit the game widget

    def game():
        global player
        random_number = number_generate()
        if random_number == 1:

            # for showing rock ,paper, scissor image

            rk_image = PhotoImage(
                file="F:\codsoft_internship\CODSOFT\\task_01\pc_rock_img.png")
            rk_img = rk_image.subsample(4, 4)
            lbl = Label(rps_wind, image=rk_img, background='#f9f7f0')
            lbl.grid(row=1, column=1)

        elif random_number == 2:

            pr_image = PhotoImage(
                file="F:\codsoft_internship\CODSOFT\\task_01\pc_paper_img.png")
            pr_img = pr_image.subsample(4, 4)
            lbl = Label(rps_wind, image=pr_img, background='#f9f7f0')
            lbl.grid(row=1, column=1)

        elif random_number == 3:

            sr_image = PhotoImage(
                file="F:\codsoft_internship\CODSOFT\\task_01\\pc_scissor_img.png")
            sr_img = sr_image.subsample(4, 4)
            lbl = Label(rps_wind, image=sr_img, background='#f9f7f0')
            lbl.grid(row=1, column=1)
        decision = check(player, random_number)
        rps_wind.mainloop()

# default image before the round start
# for users

    user_image = PhotoImage(
        file="F:\codsoft_internship\CODSOFT\\task_01\\rock_img.png")
    user_game_img = user_image.subsample(4, 4)
    user_gm_lbl = Label(rps_wind, image=user_game_img, background="#f9f7f0")
    user_gm_lbl.grid(row=2, column=1, padx=5, pady=10)

# for pc

    pc_image = PhotoImage(
        file="F:\codsoft_internship\CODSOFT\\task_01\\pc_rock_img.png")
    pc_game_img = pc_image.subsample(4, 4)
    pc_gm_lbl = Label(rps_wind, image=pc_game_img, background="#f9f7f0")
    pc_gm_lbl.grid(row=1, column=1, padx=5, pady=10)

    top_label = Label(rps_wind, justify=CENTER, text='05 POINTS TO WIN', background="#f9f7f0", fg="#72cc50", font=(
        'consolas', 20, 'bold'), width=20).grid(row=0, column=0, columnspan=3)

# for every round showing difeerent image
# rock image

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

# paper image

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

# scissor image

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

# button for users turn rock, paper , scissor

    Button(rps_wind, text='ROCK', activebackground='#f9f7f0', background='#f9f7f0', bd=0, fg='#002c3e', activeforeground='#f27777', width=7, height=2, font=('Cooper Black', 15), command=lambda: [rock_show()]
           ).grid(row=3, column=0, padx=5)

    Button(rps_wind, text='PAPER', activebackground='#f9f7f0', background='#f9f7f0', bd=0, fg='#002c3e', activeforeground='#f27777',
           width=7, height=2, font=('Cooper Black', 15), command=lambda: [paper_show()]).grid(row=3, column=1)

    Button(rps_wind, text='SCISSOR', activebackground='#f9f7f0', background='#f9f7f0', bd=0, fg='#002c3e', activeforeground='#f27777',
           width=7, height=2, font=('Cooper Black', 15), command=lambda: [scissor_show()]).grid(row=3, column=2, padx=5)

    rps_wind.mainloop()

# exit the game


def exit_wind(msg):
    rps_wind = Tk()
    rps_wind.geometry("370x400")
    rps_wind.resizable(True, True)
    rps_wind.title("RPS Game")
    rps_wind.iconbitmap(
        r"F:\codsoft_internship\CODSOFT\task_01\rps_logo.ico")
    rps_wind.config(bg='#f9f7f0')

# retry button if want to continue: image and action

    retry_img = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\retry_btn.png")
    retry_btn_img = retry_img.subsample(3, 3)
    Button(rps_wind, image=retry_btn_img, background='#f9f7f0', activebackground='#f9f7f0', borderwidth=0, compound=TOP,
           command=lambda: [rps_wind.destroy(), game_wind()]).pack(side=TOP, pady=40)

# label for show the result who win the game

    labelf = Label(rps_wind, text=msg, background='#f9f7f0', justify=CENTER,
                   fg="#72cc50", font=('jokerman', 40, 'bold'), width=9)
    labelf.place(x=30, y=145)

# exit button image and action

    exit_img = PhotoImage(
        file=r"F:\codsoft_internship\CODSOFT\task_01\exit_btn.png")
    exit_btn_img = exit_img.subsample(3, 3)
    Button(rps_wind, image=exit_btn_img, background='#f9f7f0', activebackground='#f9f7f0', borderwidth=0, compound=TOP,
           command=lambda: [rps_wind.destroy()]).pack(side=BOTTOM, pady=80)
    rps_wind.mainloop()


rps_wind.mainloop()
