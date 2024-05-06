import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html5lib")

# countries = soup.find_all("div", class_="col-md-4-country")
countries = soup.find_all("div", class_="col-md-4 country")
names_countries = countries.text.strip()
                       
print(countries)
list_countries = []
for countrie in countries:
    list_countries.append(countrie)
print(list_countries)
print(len(list_countries))

capitales = []
populations = []
surfaces = []

for capital, population, area in countries:
    capitales.append(capital)
    populations.append(population)
    surfaces.append(area)

print(capitales)

#df = pd.DataFrame(np.)


#option 1 : j'ai toutes les infos et j'essaie d'en faire un dataframe
