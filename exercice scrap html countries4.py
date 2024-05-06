import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html5lib")

countries = soup.find_all("div", class_="country")

countries = []
liste_pays = []
liste_capitales = []
liste_areas = []
liste_populations = []

for element in soup.find_all("div", class_="country"):
    #print(element.text.strip())
    countries.append(element.text.strip()) 
    name = element.find("h3").text.strip()
    liste_pays.append(name)
    capital = element.find("span", class_="country-capital").text.strip()
    liste_capitales.append(capital)
    area = element.find("span", class_="country-area").text.strip()
    liste_areas.append(float(area))
    population = element.find("span", class_="country-population").text.strip()
    liste_populations.append(int(population))
    
df = pd.DataFrame({
    "Country" : liste_pays,
    "Capital" : liste_capitales,
    "Population" : liste_populations,
    "Area": liste_areas
})

print(df)


