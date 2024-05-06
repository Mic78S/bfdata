import pandas as pd
import requests


df = pd.DataFrame([1,2, 3])
df.to_csv("test.csv")

# pour sauver une dataframe dans un fichier "test.csv"

url = "https://api.frankfurter.app/2024-03-10..?to=USD"

response = requests.get(url)
data = response.text

#on va créer un fichier avec le résultat de la requête api

file = open("dump.txt", "w")
file.write(data)
file.close()


#il y a moyen d'écrire un dictionnaire de cette manière
#ne pas oublier de le sauvegarder avec close(), ça c'est la version old school, parce que les gens oublient de fermer et sauvegarder le fichier
# à la place

with open("dump2.txt", "w") as file:
    file.write(data)

with open("dump2.txt", "r") as file:
    data = file.read()

# le truc ci-dessous est compliqué mais le formateur s'y perdait lui-même un peu
# ça permet de créer des objets qui vont s'arrêter eux-mêmes... la version old school paraît plus facile de prime abord

class MyClass:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Super objet MyClass avec number = {self.number}"

    def __enter__(self):
        print("Inside Enter!")
        return self

    def __exit__(self, *args):
        print("Inside Exit!")

m = MyClass(5)
print(m)

with MyClass(7) as truc:
    print(truc.number)


# le debuggage en mettant des points rouges dans la marge => pour utiliser Run and Debug => il se lance en prenant un peu de temps, il surligne la ligne où se trouvait le breakpoint, avec des contrôles, genre continue, passe à la ligne suivante, step into/out pour une fonction (il va dans le init) ou en sortir
# le watch permet de calculer des expressions et de voir si elles sont valides ou pas len(data) >= 20: True
test = 3
number = 0

try:
    print(test / number)
except ZeroDivisionError: 
    print("oops..")
except NameError:
    print("oops..")
except Exception as e:
    print(type(e))

print("The end")

