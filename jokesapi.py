import requests
import json

response = requests.get("https://official-joke-api.appspot.com/random_joke")

print(response.text)

print(type(response.text))

#c'est du json, ça ressemble à des dictionnaires de python et c'est tiré du javascript
# la réponse est une chaîne de caractères mais structurée
# l'objectif sera de le transformer en objet python, un dictionnaire

data = json.loads(response.text)

print(type(data))

# attention load c'est pour lire un fichier, loads pour charger une chaîne de caractères
# .loads va transformer l'objet en dictionnaire
# donc ça va marcher comme un dictionnaire, exemple : 

print(data["setup"])



