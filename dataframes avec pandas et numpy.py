import numpy as np
import pandas as pd

#les fonctions de numpy permettent des trucs différents, par exemple np.random va créer des arrays de manière aléatoire
dates = pd.date_range("2024-04-29", periods=6, freq="D")
s = pd.Series([10, 30, np.nan, 40, 62, 18], index=dates)
print([str(date) for date in dates.tolist()])

rnd = np.random.randn(6, 4)
print(rnd)
# 1 créer une dataframe 
df = pd.DataFrame(rnd)
print(df)
# on peut aussi spécifier un index à un dataframe (rnd, index=dates) ou changer le nom des colonnes => rnd, index=dates, columns=["A", "B", "C", "D"]) => les colonnes vont s'appeler A B C D

#pour récupérer une colonne entière : df["A"] ou, si le nom de la colonne ne contient pas d'espace, on peut l'appeler comme si c'était un attribut df.A
#pour récupérer une ligne entière, on peut slicer avec les index df[0:3]
# pour récupérer des données spécifiques, par exemple les données négatives, on peut indexer avec des booléens df[True, False, False, True, False, False] => Je veux récupérer la 1re et la 4e lignes
# si on a trop de lignes pour faire la liste des True, False et qu'on veut récupérer => voir fichier suivant, trop compliqué à expliquer