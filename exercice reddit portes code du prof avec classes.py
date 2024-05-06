from random import randint, choice
# pour deux éléments: from random import randint, choice (séparés par des virgules)

class Door:
    def __init__(self):
        self.open = False
        self.prize = False

#créer des instances de la classe dans une liste
doors = [Door(), Door(), Door()]
#tirer la porte au hasard
index = randint(0, 2)
winning_door = doors [index]
#Remarque : il existe d'autres fonctions importées qui permettent de simuler des nombres aléatoires, par exemple choice sur une séquence
#Option 2 : winning_door = choice(doors)
winning_door.prize = True
#Alternative: doors[index].prize = True

# pour rajouter l'étape sélection par les joueurs, on pourrait rajouter un attribut "chosen by player" dans la classe
# ici on crée une variable correspondant à l'index de la porte choisie par Bob et Alice à la première étape
chosen_by_player = 0

empty_doors = []
for i in range(len(doors)):
    if i != chosen_by_player and not doors[i].prize:
        # on pourrait écrire and doors[i].prize == False
        empty_doors.append(doors[i])

choice(empty_doors).open = True

player_switch = False

if player_switch:
    pass

if doors[chosen_by_player].prize:
    # on ne met pas == true parce que c'est un booléen
    print("You win!")
else:
    print("You lose!")

# Tout le code au-dessus correspond à une partie d'Alice. Il faut ensuite le mettre dans une fonction "def play_game()"


def play_game():
    doors = [Door(), Door(), Door()]
    index = randint(0, 2)
    winning_door = doors [index]
    winning_door.prize = True
    chosen_by_player = 0
    empty_doors = []
    for i in range(len(doors)):
        if i != chosen_by_player and not doors[i].prize:
            empty_doors.append(doors[i])
    choice(empty_doors).open = True
    player_switch = False
    if player_switch:
        pass
# Ci-dessous, on voit comment rappelr les réusltats
    if doors[chosen_by_player].prize:
        return True
    else:
        return False
# autre manière de l'écrire puisqu'il s'agit d'une valeur booléenne
    # return doors[chosen_by_player].prize

win_total = 0
for i in range(1000):
    win = play_game()
    if win:
        win_total += 1

# autre manière de l'écrire
# for i in range(1000):
    # if play_game():
        # win_total += 1

print(f">on {win_total} times.")

