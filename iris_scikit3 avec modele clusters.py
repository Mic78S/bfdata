from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.decomposition import PCA
# ci dessous pour représenter les données en blops gaussiens, pour le clustering
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import numpy as np

# ici, on va voir un modèle non supervisé, le clustering, dont l'objectif est de voir si les données se rassemblent en différents groupes et combien

iris = load_iris()
X_iris = iris.data
y_iris = iris.target


X_train, X_validate, y_train, y_validate = train_test_split(X_iris, y_iris, test_size=0.5)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)

y_predict = model.predict(X_validate)
score = accuracy_score(y_validate, y_predict)

print(accuracy_score(y_validate, y_predict))

scores = cross_val_score(model, X_iris, y_iris, cv=8)
print(scores)

print(scores.mean())


model_pca = PCA(n_components=3)
model_pca.fit(X_iris, y_iris)
X_2D = model_pca.transform(X_iris)
print(X_2D)

#plt.scatter(X_2D[:, 0], X_2D[:, 1], c=y_iris)
#plt.show()


#ici on va instancer le modèle mais on doit quand même lui dire combien de groupes on veut à la fin (n_components), combien on veut de blops

model_gm = GaussianMixture(n_components=3)
# on va fitter l'instance aux données uniquement avec les x
model_gm.fit(X_iris)
# je n'ai pas compris la ligne suivante, à chercher
y_gm = model_gm.predict(X_iris)

#ici on va utiliser les couleurs données pour y_gm
plt.scatter(X_2D[:, 0], X_2D[:, 1], c=y_gm, alpha=0.6)
# on rajoute un paramètre d'opacité alpha=0.6 pour essayer de distinguer les séries de points
# on obtient plus ou moins la même chose que dans iris_scikit2 sans avoir jamais donné les y (= précisé les espèces)
plt.scatter(X_2D[:, 0], X_2D[:, 1], c=y_iris, alpha=0.4)

plt.show()






