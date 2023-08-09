import random


def number_generate():
    random_number = random.randint(1, 3)
    return random_number


def check(player, pc):
    if (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
        return "YOU WIN"
    if (player == 1 and pc == 2) or (player == 2 and pc == 3) or (player == 3 and pc == 1):
        return "PC WIN"
    return "DRAW"


def game(choice):
    if choice == 1:
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
    else:
        return "Thank You"


print("Start[1] | Exit[0]")
choice = int(input())
result = game(choice)
print(result)
