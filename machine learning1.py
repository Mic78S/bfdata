import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(42)
# le nombre 42 est une "seed", une base qui va faire que RandomState donnera toujours la même série de nombres "aléatoires"
x = rng.rand(40)*10
# .rand crée une situation random entre 0 et 1 => rand(40) sera un tableau de 0 et de 1
# cela reste un vecteur linéaire, un tableau à 1 dimension qui ne contient que 40 éléments
# ci-dessous, on crée une droite (y=2*x-1)
y = 2 * x-1 +rng.randn(40)
# randn(40) va créer une petite variabilité de 0 à 1 sur les différents points qui composent la droite

# Les paramètres donnés quand on instancie le modèle, les paramètres de départ (par exemple, les caractéristiques spécifiques de la droite qui représente les données) sont appelés hyper paramètres

model = LinearRegression(fit_intercept=True)
# : signifie tous les éléments, sans préciser les débuts et fins ; np.newaxis sert à ajouter une dimension au tableau
X = x[:, np.newaxis]

print(X.shape)
# avec le print ci-dessus, on peut voir que X est maintenant un tableau avec 40 lignes et 1 colonne (2 dimensions) alors que x ne contenait que 40 lignes (1 dimension)

model.fit(X, y)

print(f"Model params: coeff {model.coef_} intercept {model.intercept_}")

# print(model.coef_)
# print(model.intercept_)

xfit = np.linspace(-1, 11, 20)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit, "r-")
plt.show()
