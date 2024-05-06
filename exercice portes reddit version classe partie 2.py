from random import randint, choice

class Door:
    def __init__(self):
        self.open = False
        self.prize = False

doors = [Door(), Door(), Door()]

def play_game(first_door, switch_door):
    index = randint(0, 2)
    winning_door = doors[index]
    winning_door = choice(doors)

    winning_door.prize = True

    chosen_by_player = first_door

    empty_doors = []
    for i in range(len(doors)):
        if i != chosen_by_player and not doors[i].prize:
            empty_doors.append(doors[i])

    choice(empty_doors).open = True

    if switch_door:
        for i in range(len(doors)):
            if i != chosen_by_player and not doors[i].open:
                chosen_by_player = i
                # pour stopper la boucle
                break
            
    return doors[chosen_by_player].prize

player_switch = False

win_total = 0
for i in range(10000):
    if play_game(0, True):
    win_total += 1
    

if doors[chosen_by_player].prize:
    print("You win!")
else:
    print("You lose!")

