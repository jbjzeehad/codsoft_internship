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

#    else:
#        return "PC WIN"
#    elif player == 1 and pc == 2:
#        return "PC WIN"
#    if player == 2 and pc == 1:
#        return "YOU WIN"
#    else:
#       return "PC WIN"
#    elif player == 2 and pc == 3:
#        return "PC WIN"
#    if player == 3 and pc == 1:
#       return "PC WIN"
#    else:
#        return "YOU WIN"
#    elif player == 3 and pc == 2:
#        return "YOU WIN"


print("Rock[1], Paper[2], Scissor[3]: ")
user = int(input())
random_number = number_generate()
print("PC choose: " + str(random_number))
decision = check(user, random_number)
print(decision)
