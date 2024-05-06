# step1: les portes ont deux attributs possibles ouverte/ fermée et prix/rien
# tirer un nombre au hasard entre 1 et 3 qui désigne la porte dont l'attribut est prix, puis le stocker en mémoire
# les trois portes ont l'attribut fermé
# step2: Alice choisit une porte et Bob choisit une porte
# step3: une des trois portes a l'attribut est ouverte, elle est différente des choix de Bob et d'Alice et de celle tirée au hasard
# step4: Bob change de porte
# step5: comparer les choix d'Alice et de Bob au nombre tiré au hasard. Celui qui correspond gagne la partie.
# step5: boucle for in range(1000) sur les succès accumulés de Bob et d'Alice. Comparer les deux.

from random import randint

class Porte():
    def __init__(self, state, number):
        self.state = bool()
        self.number = range(1,3)

def 

    