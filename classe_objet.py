#class Calculator: 
 #   def __init__(self):
#        self.result = 0

 #   def add(self):
  #      self.result += 1

# pour créer une instance de la classe, il faut l'appeler comme une fonction

#calc = Calculator()
#print(calc.result)
#calc.add()
#print(calc.result)

# on va ajouter un argument à add pour lui dire de combien on veut augmenter

class Calculator: 
    def __init__(self, initial_value =0):
        self.result = initial_value

    def add(self, amount):
        self.result += 1

# self => ce qui compte, ce n'est pas son nom, c'est sa place
# c'est le premier argument qui crée l'instance

calc = Calculator()
print(calc.result)
calc.add(5)
print(calc.result)

calc = Calculator(10)
print(calc.result)
calc.add(5)
print(calc.result)

# on peut aussi faire un return sur une méthode. A part le fait qu'elles opèrent dans une classe, 
# et que du coup elles ont l'argument self, les méthodes fonctionnent comme des fonctions.
 