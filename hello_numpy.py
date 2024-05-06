import numpy as np

numbers = [1, 2, 3]
print(numbers * 5)
# Regarde le résultat si tu as oublié. Pourquoi c'est parfois pénible les listes.

# pour les données des arrays dans numpy, on écrit les données sous forme de séquences, ci dessous une liste

a = np.array([1, 7, 12])
print(a)
print(a * 5)

# tableau avec deux lignes et trois colonnes

b = np.array([[1.5, 2, 5], [1, 7 , 42]])
print(b)
# numpy a détecté qu'il y avait un float dans une liste, donc il a transformé tous les entiers en floats (2. 5. etc., sous-entendu 2.00 5.00 etc.)

# pour aller chercher l'index d'un tableau : s'il n'y a qu'une seule ligne, ça fonctionne comme une liste; si il en y a plusieurs, ça fonctionne comme ci-dessous

print(b[1, 0]) # Ligne, puis colonne

z = np.zeros((5,7))
print(z)

#on peut multiplier les listes entre elles mais ça ne fonctionne pas si le nombre de colonnes dans un tableau est différent du nombre de colonnes dans un autre tableau

#pour modifier les valeurs d'un tableau, c'est comme pour un tableau, avec l'index 
b[0, 2] = 15

#pour créer des tableaux avec un "décompte"
numbers = np.arange(10)
print(numbers)
# avec trois arguments, ça va être comme range, début, le pas (l'éccart entre chaque nombre, par exemple pair ou impair)
numbers2 = np.arange(1, 11, 2)
print(numbers2)
# sur arange il y a une méthode qui permet de donner aux données la forme que l'on veut, par exemple 3 lignes, 2 cikibbes
#attention, ça ne modifie pas le tableau, ça lui donne juste une forme
numbers2.reshape((3, 2))
# pour modifier le tableau, il faut réassigner la valeur
numbers2 = numbers2.reshape((3, 2))

#sympa, surtout pour les graphiques, regarde :
print(np.linspace(0, 10, 4))




