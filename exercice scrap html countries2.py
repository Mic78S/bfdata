import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html5lib")

# countries = soup.find_all("div", class_="col-md-4-country")
countries = soup.find_all("h3", class_="col-md-4 country")
capitales = soup.find_all("span", class_="country-capital")
populations = soup.find_all("span", class_="country-population")
surfaces = soup.find_all("span", class_="country-area")

#print(type(capitales))                      
#print(countries)
list_countries = []
list_areas = []
list_populations = []
list_capitals = []

#for span_tag in soup.find_all("span", class_="country-capital"):
 #   print(span_tag.text, span_tag.next_sibling)

for pays in soup.find_all("h3", class_="col-md-4 country"):
    pays.text.strip()
    list_countries = pays.text.strip()

#print(list_countries)

for capitale in soup.find_all("span", class_="country-capital"):
    capitale.text.strip()
    list_capitals = capitale.text.strip()

print(list_capitals)

for population in soup.find_all("span", class_="country-population"):
    population.text.strip()
    list_populations = population.text.strip()

for area in soup.find_all("span", class_="country-area"):
    area.text.strip()
    list_areas = area.text.strip()


df = pd.DataFrame(index=countries, columns=[capitales, populations, surfaces])
print(df)



#names_countries = capitales.tag.contents
#print(list_countries)

#print(names_countries)

#for countrie in countries:
 #   list_countries.append(countrie)
#print(list_countries)
#print(len(list_countries))


populations = []
surfaces = []

#for capital, population, area in countries:
  #  capitales.append(capital)
   # populations.append(population)
    #surfaces.append(area)

#print(capitales)

#df = pd.DataFrame(np.)


#option 1 : j'ai toutes les infos et j'essaie d'en faire un dataframe
