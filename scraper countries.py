import requests
from bs4 import BeautifulSoup
# on a besoin uniquement de la classe BeautifulSoup ; écrire à chaque fois bs4.BeautifulSoup serait pénible

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text, "html5lib")

# html5lib est intégré à BeautifulSoup. On n'a pas besoin de l'importer directement.

titles = soup.find_all("h1")
# C'est une liste, avec un seul élément ! du coup title = soup.find("h1") fonctionnerait donc tout aussi bien

title = soup.find("h1")

print(title)
print(len(title))
print(titles[0].text)
print(title.text)

txt = title.text.strip()

#pour retirer les espaces avant 250 items

while "   " in txt:
    txt = txt.replace("   ", "   ")

print(txt)

for noms_de_pays in soup.find_all("h3"):
    print(noms_de_pays.text.strip())











