from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
# ci dessous, la méthode importée permet de vérifier des ensembles de données
from sklearn.metrics import accuracy_score
# la méthode ci-dessous permet de couper le set de données en deux : une partie pour entraîner, une partie pour vérifier
from sklearn.model_selection import train_test_split, cross_val_score

import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X_iris = iris.data
y_iris = iris.target

# ou alors X_iris, y_iris = load_iris(return_X_y=True)

# les colonnes se sont les caractéristiques des fleurs tandis que les nombres à la fin sont les trois espèces classifiées

#pour diviser le set de données en deux. test-size=0.5 => la moitié des données pour tester l'autre moitié pour entraîner
X_train, X_validate, y_train, y_validate = train_test_split(X_iris, y_iris, test_size=0.5)

# pour avoir toujours le même résultat, il faut que le train_test_split soit choisi à partir d'un nombre fixe => random.state = un nombre (random.state = 42) Sinon, il répartit les données en deux groupes de manière aléatoire et les résultats ne seront pas forcément les mêmes

# pour être sûr de ses résultats, il faut faire de la crossvalidation avec cross_val_score !

#print(X_iris)
#print(y_iris)

#model = GaussianNB()
# ci-dessous, c'est une manière de montrer en quoi c'est un problème de réutiliser les mêmes données pour la vérification => il va donner une précision de 100%
# une bonne manière de faire est de garder une série de données sur le côté, pour les utiliser par après en vérification
model = KNeighborsClassifier(n_neighbors=1)
#model.fit(X_iris, y_iris)
# pour vérifier
model.fit(X_train, y_train)


#pour vérifier si le modèle marche, on peut utiliser:
#y_predict = model.predict(X_iris)
#print(accuracy_score(y_iris, y_predict))
# ça donne 0.96, ce qui est un très bon score

# avec une partie des données gardée pour tester
y_predict = model.predict(X_validate)
print(accuracy_score(y_validate, y_predict))

# avec cross_val_score, il faut commencer par lui donner le modèle et le dataset en entier, puis l'attribut cv => soit un nombre entier (le nombre de sets de données divisés pour la crossverification) ou 
scores = cross_val_score(model, X_iris, y_iris, cv=5)
print(scores)

# pour avoir une idée du score moyen : (le plus proche d'une vraie mesure de la qualité du truc)
print(scores.mean())

# ça permet de mieux choisir les paramètres en fonction du niveau de validation
# bien entendu, au final, on va tester le modèle sur toutes les données, on ne va pas en laisser une partie de côté, mais ça permet de vérifier




