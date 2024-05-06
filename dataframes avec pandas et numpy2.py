import numpy as np
import pandas as pd

dates = pd.date_range("2024-04-29", periods=6, freq="D")
s = pd.Series([10, 30, np.nan, 40, 62, 18], index=dates)
print([str(date) for date in dates.tolist()])

rnd = np.random.randn(6, 4)
print(rnd)

df = pd.DataFrame(rnd, index=dates, columns=["A", "B", "C", "D"])
print(df[df["A"] > 0])
# ça permet de récupérer les données d'un dataframe en se basant sur des comparaisons appliquées à une colonne (ici, la colonne A) et de les afficher dans une autre dataframe (filtrer)
# il y a moyen de filtrer avec plusieurs critères mais la syntaxe est plus compliquée qu'ajouter un nouveau truc

# dictionnaire qui contient nos data
data = {
    "User": ["user1", "user2", "user4"],
    "Score" : [15, 75, 0]
}
# Ensuite on crée une dataframe qui contient le dictionnaire

scores = pd.DataFrame(data)
print(scores)



