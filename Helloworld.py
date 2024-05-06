print("Hello, world !")
variable = 3
print(type(variable))
if "message"<"texte":
    print("True")
variable2 = "Salut"
if variable2:
    print("OK!")

variable3 = "test"
if variable3:
    print("Ok!")
    variable3 = ""
else:
    print("Not Ok")

a = 3
b = 5
if a > b:
    print(str(a) + " est plus grand que " + str(b))
elif a == b:
    print(f"{a} est égal à {b}")
else:
    print(f"{a} est plus petit que {b}")

a = 0
while a < 10:
        print(a)
        a += 1
        # La fonction suivante va se faire à chaque fois avant de recommencer la boucle.
        # print("---")

#while True:
 #   pass

three = 3
my_list = [4, 5, 6]
weird_list = [1, "two", three, my_list]
print(weird_list)
print(weird_list[1])
print(weird_list[1:3])

words = ["I", "really", "love", "python"]
print(words[:2])
print(words[2:])

words1 = ["I", "really", "love", "python"]
index = 3
print(words1[:index])
print(words1[index:])

print(len(words))

numbers = [42, 12345, 987, 546]
numbers.append(50)
numbers.append(51)
numbers.insert(0, 10000)
print(numbers)

# Pour retirer tous les éléments d'une liste, on peut faire une boucle
numbers2 = [42, 12345, 987, 42, 42, 546]
while 42 in numbers2:
    numbers2.remove(42)
print(numbers2.pop(2))
print(numbers2)

index = numbers2.index(987)
print(index)

print(numbers2[1])

range(10)

num = range(10)
print(num)
# Python a créé un objet générateur qui permet de créer tous les nombres de 0 à 9.
print(list(num))
# Python a transformé l'objet range en objet liste, ce qui fait qu'il affiche tous les nombres de 0 à 9

num2 = range(10000000)
print(num2)
# l'afficher prendrait trop de temps mais ça permet de stocker un grand nombre de nombres

from random import randint
from unicodedata import name

def dice():
    result = randint(1, 6)
    return result
print(dice(), dice())

def dices(amount=1, face=6):
    result = 0
    for _ in range(amount):
    # _ est une manière de donner un nom à la variable qui permette au lecteur
    # de savoir que la variable n'a aucune utilité en dehors de la boucle for
        result += randint(1, face)
    return result
print(dices(2, 8))

def dice2(dice_number, faces=6):
    total = 0

    for i in range(dice_number):
        result = randint(1, faces)
        total += result
    return total

# __class__.__name__ permet de connaître le nom et le classe d'un objet
a = 3
print(a.__class__.__name__)
b = (3, 7, 8)
print(b.__class__.__name__)






def double(number):
    return number *2
   #number est l'argument

value = double(5)
# 5 est le paramètre qui attribue une valeur à l'argument


 
 
#par défaut, quand on crée une variable dans une fonction, elle reste locale

test = 3
def myfunction():
    test = 4
    print(f"Test dans myfunction: {test}")

myfunction()

print(f"Test en dehors de myfunciton : {test}")

# pour que la variable devienne globale, on utilise global








