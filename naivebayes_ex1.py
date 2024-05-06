from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import numpy as np


# blobs permet de créer des groupes de données plus ou moins séparés les uns des autres
# les arguments : créer 100 points en 2 groupes, le nombre de centres de chaque points, seed du générateur de nombres, écart type)
X, y = make_blobs(100, 2, centers=2, random_state=2, cluster_std=1.5)

model = GaussianNB()
model.fit(X, y)

#ci-dessous, on va devoir générer aléatoirement des points un plein d'étapes; dans numpy, tout se fait/se calcule élément par élément
rng = np.random.RandomState(42)
Xnew = [-6, -14] + [14, 18] * rng.rand(2000, 2)
# ici, 2000 lignes et 2 colonnes, c'est déjà un graphique à deux dimensions ; pas besoin d'en rajouter de nouvelles
ynew = model.predict(Xnew)


# les arguments de scatter X[:, 0] toutes les lignes de la colonne 0 vs toutes les lignes de la colonne 1 ; c=y c'est la couleur qui est donnée par y
# cmap est une façon de définir les couleurs : RdBu red down blue up et s la saturation
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="RdBu", s=50)
plt.scatter(Xnew[:, 0], Xnew[:, 1], c=ynew, s=50, alpha=0.1)

# l'alpha à la fin, c'est pour l'opacité des points, pour mieux visualiser les nouvelles données

plt.show()
