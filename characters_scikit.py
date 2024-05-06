from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
import matplotlib.pyplot as plt

# on a 1800 entrées dans load_digits, on va créer des subplots plus petits pour pouvoir les gérer
# le 3e argument est pour donner une taille à la figure (à chacune des sous-parties, 8 pixels sur 8 dans le dataset load_digits)
# subplot_kw={} pour donner des arguments à chacun des subplots sous forme d'un dictionnaire (xticks et yticks, c'est la gradation des axes x et y)
# gridspec_kw à chercher mais en gros pour avoir tous les éléments les uns à côté des autres
fig, axes = plt.subplots(10, 10, figsize=(8, 8), subplot_kw={"xticks":[], "yticks":[]}, gridspec_kw={"hspace":0.1, "wspace":0.1})
# maintenant on a un array numpy (pas de virgules) de 10 sur 10
# .flat chez numpy permet de créer un itérateur qui permettra de faire une boucle plus facilement (?)


digits = load_digits()


for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="binary")
    ax.text(0.05, 0.05, str(digits.target[i]), transform=ax.transAxes, color="green")
fig.show()


#passer de données "images" à des données numériques (quand c'est noir et blanc, c'est un pixel noir ou blanc)
X = digits.data
y = digits.target

# la pca, c'est faire passer un espace en 3D en 2D
# celle qu'on va utiliser, c'est la même chose mais ça permet en plus de plier la feuille (par exemple, pour faire une spirale)
# instancer la classe (n components précise le nombre de dimensions des données, 2 puisqu'on veut afficher)
model_iso = Isomap(n_components=2)
model_iso.fit(X)
X_iso = model_iso.transform(X)

#il faut refaire une 2e figure sinon il reste coincé sur la précédante
# on va chercher toutes les couleurs du spectre avec cmap...

plt.figure()
plt.scatter(X_iso[:, 0], X_iso[:, 1], c=y, cmap=plt.cm.get_cmap("Spectral", 10))
plt.colorbar(ticks=range(10))
plt.show()

input()

#la fonction enumerate permet de recevoir les trucs dans des tuples


