
#%%
# pour avoir des infos sympas sur le contenu #%% run cell puis variable dans la fenêtre qui s'ouvre
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

response = requests.get("https://api.frankfurter.app/2024-03-10..?to=USD")

data = json.loads(response.text)

print(data)
print(type(data))

data2 = data["rates"]

print(data2)

# x = pd.date_range("2024-03-11", periods=50)
# y = pd.json_normalize(data2, max_level = 2)
# il faudrait que je voie si ça marche avec json.normalize pour essayer de le faire en deux lignes

# print(x)
# print(y)


#le dictionnaire s'appelle rates et les clés sont les dates

dates = [] 
#dates = list(data2.keys())
#taux = list(data2.values())

taux_usd = []

for date, rate in data2.items():
  # dates.append(date)
  dates.append(pd.to_datetime(date))
  taux_usd.append(rate["USD"])

df = pd.DataFrame({"Date": dates, "USD": taux_usd})



print(dates)
# print(taux)

plt.plot(df["Date"], df["USD"], "b.-")
plt.show()

# pour éviter l'absence des jours de weekend, il y a plusieurs possibilités. Le module datetime de python pourrait fonctionner.
# dans la boucle for, all_dates.append(datetime.datetime.strptime(date, "%Y-%m-%d")) ou (pd.to_datetime(date))



# %%
