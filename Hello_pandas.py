import numpy as np
import pandas as pd

# s = pd.Series([10, 30, 20, 40, 62, 18])
# pandas signale que Series est une classe
#print(s)

# pandas donne la liste en donnant les index, le type et le fait que c'est encodé en 64 bits

# à la différence d'une liste python, ça permet de conserver les index originaux ! Si je sélectionne deux éléments de la série et que je les extrait, ils gardent les index qu'ils avaient dans la série
# si c'était une liste, ces deux éléments formeraient une nouvelle liste qui aurait les index 0 et 1

#s_list = [10, 30, 20, 40, 62, 18]
#s_list[2: 4]
#s[2:4]

#np.nan permet d'inclure des éléments qui ne sont pas des nombres entiers classiques sans modifier le type de la série
# cette dernière partie est moins claire

# 10 minutes pour apprendre pandas, pour la doc 
# les séries indexées par des dates sont des times series

dates = pd.date_range("2019-07-09", periods = 6)
# plein d'arguments possibles après date_range, mais le premier est toujours start, format iso est le moins ambigu année mois jour (en plus, c'est pratique si on se retrouve avec des dates en chaînes de caractères 
# parce que le classement par ordre chronologique)
# periods= il faut un keyword, pour passer le 2e attribut
# attention, il ne faut pas oublier de préciser que l'index = dates
s = pd.Series([10, 30, 20, 40, 62, 18], index=dates)
print(s)

#Mes frequences d'intervales = freq="D" pour jour, freq="ME" pour mois, il y en a beaucoup, B pour business day frequency, W pour semaine, YE fin de l'année, YS début de l'année, D3 pour trois jours, h pour les heures
# print([str(date) for date in dates.tolist()]) => compliqué mais intéressant, à fouiller
#  

