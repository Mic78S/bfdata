from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
# ça, c'est pour simplifier le truc, voir page 12 partie 8 (la spirale)
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# pour représenter ces données, le problème est qu'il y a 4 caractéristiques de fleurs et que ça ferait un graph à 5 dimensions
# on va donc essayer de passer les données à deux dimensions ! Attention ! Ne pas oublier que le résultat n'aura un sens que numérique, 
    # ça ne correspondra pas à une nouvelle catégorie, une nouvelle variable, ça va juste permettre de bien voir qu'il y a deux groupes de données

iris = load_iris()
X_iris = iris.data
y_iris = iris.target


X_train, X_validate, y_train, y_validate = train_test_split(X_iris, y_iris, test_size=0.5)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

y_predict = model.predict(X_validate)
print(accuracy_score(y_validate, y_predict))

scores = cross_val_score(model, X_iris, y_iris, cv=8)
print(scores)

print(scores.mean())

#ci dessous, on va limiter le modèle à 2 dimensions (plus les couleurs pour les groupes de données), ce qui est visible sur un graphique
model_pca = PCA(n_components=2)
model_pca.fit(X_iris, y_iris)
X_2D = model_pca.transform(X_iris)
# ce n'est pas une prédiction, on va transformer les données
#ci dessous, on verra bien qu'il a transformé tout ça en tableau à 2 colonnes
print(X_2D)

#ci dessous le c va permettre de reprendre les trois catégories de fleurs (les colonnes)
# ça ne permet pas d'interpréter les données mais de les vérifier et de comprendre un peu ce qui se passe avec les différents groupes de données
plt.scatter(X_2D[:, 0], X_2D[:, 1], c=y_iris)
plt.show()






