
# pour expliquer à matplotlib qu'on va l'utiliser pour autre chose que l'interface graphique et éviter les messages d'erreur, et utiliser uniquement sa version light qui gère les données

import matplotlib
# on va lui demander d'utiliser une backend non interactive (agg dans ce cas-ci, mais ça pourrait être du svg - se renseigner sur comment faire du svg) ; agg = antigrade geometry
matplotlib.use("agg")


import dash
# pour éviter de taper dash.import à chaque fois (rappel)
from dash import html, dcc
from dash.dependencies import Input, Output
from plotly.tools import mpl_to_plotly
import matplotlib.pyplot as plt
import numpy as np


# ci dessous, le texte contenu dans le div doit changer en fonction du texte dans l'input
# la plupart des dcc, des éléments, le composant qu'on va changer se trouve dans value

# attention ! ne pas oublier que "children" contient le contenu de l'élément
# dans @app.callback(Output(component_id="my-div")), le component n'est pas obligatoire, le id est suffisant
# un seul output mais plusieurs inputs (d'où une liste) ; si on veut que plusieurs choses changent, il faut créer deux fonctions app

# le bouton callback dans dashboard est génial !

app = dash.Dash()

# on remplace le 3*np.pi par n*np.pi et on met n en argument, sans oublier de lui donner une valeur par défaut (n=3), parce que c'est ça qu'on va vouloir modifier avec le slider
def create_sine_graph(n=3):
    fig, ax = plt.subplots()
    x = np.arange(0, n*np.pi, 0.1)
    ax.set_title("Sine Wave Form")
    ax.plot(x, np.sin(x), "r--")
    return mpl_to_plotly(fig)

app.layout = html.Div([
    html.H1("First Dash app"),
    html.H3("Bruxelles Formation 2024"),
    dcc.Slider(0, 20, 2, value=10, id="graph-slider"),
    #le value=10 va mettre le curseur à 10 par défaut
    dcc.Graph(figure=create_sine_graph(), id="sine-graph"
)
])

# ci dessus, on appelle la fonction qui crée le graph une seule fois, donc pour connecter le slider au graph il va falloir créer un truc qui réagit à de nouveaux événements => un callback
# on va créer une fonction qui va renvoyer une valeur qui va updater / modifier la propriété d'un autre élément et updater le graph quand on le change (def update...)
# et une fonction avec une entrée et une sortie, en lui donnant l'id du composant qu'on veut modifier et, en deuxième argument, la propriété qu'on veut changer
@app.callback(Output("sine-graph", "figure"), [Input("graph-slider", "value")]
)
#le @app.callback modifie la fonction qui vient après ! S'il n'y a rien après => message d'erreur 
def update_sine_graph(slider_value):
    return create_sine_graph(slider_value)


if __name__ == "__main__":
    app.run(debug=True)



