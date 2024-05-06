from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np


fig, axes = plt.subplots(10, 10, figsize=(8, 8), subplot_kw={"xticks":[], "yticks":[]}, gridspec_kw={"hspace":0.1, "wspace":0.1})

digits = load_digits()


for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap="binary")
    ax.text(0.05, 0.05, str(digits.target[i]), transform=ax.transAxes, color="green")
fig.show()


X = digits.data
y = digits.target

model = GaussianNB()
X_train, X_validate, y_train, y_validate = train_test_split(X, y, test_size=0.25)

# c'est la ligne suivante qui me manquait !!!
model.fit(X_train, y_train)
y_predict = model.predict(X_validate)
score = accuracy_score(y_validate, y_predict)
print(score)
confusion = confusion_matrix(y_validate, y_predict)
print(confusion)

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.get_cmap("Spectral", 10))
plt.colorbar(ticks=range(10))
plt.show()

input()




