import requests

response = requests.get("https://api.parrycarry.com/coin/flip")
# response, c'est juste le nom de la variable dans laquelle on la stocke
print(response)

# le code 200, c'est comme le 404 (erreur 400 quelque chose = on a pas trouvé la page ; erreur 500 serveur inaccessible), sauf que ça veut dire que tout est ok
print(response.text)
# ça donne le contenu de la page (le code html)