import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

folder = Path(__file__).parent
file = Path(folder, "social_network_data.csv")

df = pd.read_csv(file)

print(df["friends"].value_counts())
df_filtered=(df["friends"]<100)


#plt.plot(df["friends"])
# plt.show()

#pour trier par colonne par ordre croissant
#df.sort_values(by=["minutes"])
#print(max(df["friends"]))
# pour trier par colonne par ordre décroissant
#print(df.sort_values(by=["friends"], ascending=False))
print(df.mean())
print(df.median())
print(df.quantile(0.75))
print(df.quantile(0.25))
print(df.var())
#cette dernière méthode va donner l'ecart type des données
print(df.std())
print(df.describe())

#pour récupérer le début d'une dataframe, .head() avec le nombre de lignes qu'on veut entre parenthèses et tail() pour les dernières lignes
print(df.head(5))
print(df.tail(3))
print(df.cov())
print(df.corr())


plt.scatter(df["friends"], df["minutes"]) 

#pour la variance, si on met les eccarts au carré, c'est pour éviter les négatifs


counts = df["friends"].value_counts()
#print(counts)
#plt.bar(counts.index, counts)
#plt.show()

#coeff = np.polyfit(x, y, deg)
#deg = degré 1 pour une droite; degré 2 pour une parabole ; degré 3 pour x au cube
coeff = np.polyfit(df["friends"], df["minutes"], 1)
#avec un degré 1, le polygone mettra en évidence la corrélation entre "friends" et "minutes"
# pour reorésenter la racine carrée, il suffit d'inverser x et y !!! Pourquoi ? A chercher !!!
p = np.poly1d(coeff)
x = np.linspace(0, 100, 100)
# pour le dernier nombre, il faut qu'il y en ai plus que 100 pour pouvoir dessiner la courbe entre les points
# avec p(3) ça calculera la valeur du polynome si x = 3
plt.plot(x, p(x), "ro")
plt.show()

#la page 14 du 7, j'ai rien compris
