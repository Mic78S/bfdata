from random import randint


class Portes():
    def __init__(self, x):
        if x == True:
            x = 1
        elif x == False:
            x = 0 


class Portes_step():
    def __init__(self, amount, x):
        number = randint(1, amount)
        if number == x:
            result =+ 1
        else:
            result = 0
        return result 

class Portes_step1(Portes_step):
    def __init__ (self):
        super().__init__(3, 1)

class Portes_step2_alice(Portes_step):
    def __init__ (self):
        super().__init__(2, 1)

class Portes_step2_bob(Portes_step):
    def __init__(self):
        super().__init__(2, 2)

victoires_alice = 0
victoires_bob = 0

for i in range(1000):
    victoires_alice = victoires_alice + Portes_step1()
    victoires_bob = victoires_bob + ()


