import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# pour créer un chemin absolu vers le fichier, on va télécharger pathlib et la classe Path, puis créer une instance de la classe Path en lui ajoutant __file__ et la méthode .parent
# pour que le chemin du fichier soit toujours le même s'il est dans le même répertoire
# ça marchera tant que les deux fichiers seront dans le même répertoire

# si je veux le mettre dans un autre répertoire dataframe = pd.read_csv(Path(file_path,"data", "countries.csv"))
# pour les deux, cela demanderait plus de code : il faudrait faire une exception pour qu'il cherche un endroit et puis cherche dans un autre s'il ne le trouve pas dans le premier

file_path = Path(__file__).parent

# print(file_path.parent)


# print(__file__)

df = pd.read_csv(Path(file_path, "countries.csv"))



#graphique = pd.Series(

# ["Country"], ["Name"], ["GDPPC"], ["Literacy"])
x = df["Name"]
y = df["Literacy"]

plt.xlabel("Pays")
plt.ylabel("Taux d'alphabétisation")
plt.plot(x, y)
plt.show()

#plt.scatter(x, y) donne des points par défaut

# print(dataframe)

# rapport entre alphabétisation et pib par habitant, 4 colonnes et 171 lignes 
# print(dataframe["Country", "Name", "GDPPC", "Literacy"])
