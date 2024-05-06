import matplotlib.pyplot as plt

plt.plot([-10, -1, 3, 7], [1, 3, 2, 4])
plt.ylabel("Some numbers")
# ylabel va donner un label à l'axe y du graphique
plt.show()
# sans plus d'infos, il place les numéros y sur les numéros de l'axe x correspondant aux index de la liste
# pour modifier le styler, on rajoute un truc après les données plt.plot([-10, -1, 3, 7], [1, 3, 2, 4], "ro") => ro crée des points ronds plutôt que des lignes

# important ! les coordonnées de l'axe y s'adaptent aux données du graphique, ce qui rend difficile la comparaison de deux graphiques différents ayant des données différentes en axe y
# pour éviter ça plt.axis : 
# plt.axis([x_min, x_max, y_min, y_max])
# plt.axis([0, 6, 0, 20])




