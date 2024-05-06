from turtle import speed


#class Bike:
 #   def __init__ (self, distance, speed):
  #      speed = 15
   #     distance = 0

    #def ride(self):
     #   self.result = Bike(distance) * Bike(speed)


#class Bike:
 #   def __init__(self):
  #      self.speed = 15
   #     self.distance = 0

    #def ride(self, duration):
     #   travel = self.speed * duration
      #  self.distance += travel
        
#class Car:
 #   def __init__(self):
  #      self.speed = 100
   #     self.distance = 0

    #def ride(self, duration):
     #   travel = self.speed * duration
      #  self.distance += travel

# les deux codes sont quasi identiques. Ici, on peut affirmer que les cars sont des véhicules ayant une vitesse de 100 et les bikes sont des véhicules ayant une vitesse de 15.

class Vehicule:
    def __init__(self, speed):
#Attention = self.speed et speed sont deux éléments différents.    
        self.speed = speed
        self.distance = 0

    def ride(self, duration):
        travel = self.speed * duration
        self.distance += travel
        

class Bike(Vehicule):
    #dit à python qu'on reprend tout ce qui est inclut dans la classe vehicule dans la classe bike, plus ce qui va suivre.
    def __init__(self):
        super().__init__(15)


class Car(Vehicule):
    def __init__(self):
        super().__init__(100)
# va chercher l'initiative de la classe parent et lui donne une valeur de 15
# par convention, on commence par la fonction super(), sauf si on a une bonne raison de faire autrement
        self.fuel = 100
        self.consumption = 0.05

    def ride(self, duration):
        travel = duration * self.speed
        travel_max = self.fuel / self.consumption
        # min() permet de sélectionner la valeur minimale (la plus basse), entre deux paramètres
        travel = min(travel, travel_max)
        super().ride(duration)
        self.distance += travel
        self.fuel -= self.consumption * travel

class Train(Vehicule):
    def __init__(self):
        super().__init__(50)

bike = Bike()
bike.ride(1)
print(bike.distance)
car = Car()
car.ride(.250)
print(car.distance)
print(car.fuel)


