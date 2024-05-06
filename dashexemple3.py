import dash
# pour éviter de taper dash.import à chaque fois (rappel)
from dash import html, dcc
from plotly.tools import mpl_to_plotly
import matplotlib.pyplot as plt
import numpy as np
# pour pouvoir utiliser des graphiques matplotlib dans un dash


#on crée une instance de la classe Dash
app = dash.Dash()
#on lui donne un layout minimum (ici, un Div), parce que dash en a besoin
# on peut mettre du texte dans le Div, mais on peut aussi mettre du html et du cass
#app.layout = html.Div("Hello everyone !")
#app.layout = html.Div(html.H1("First Dash app"))
#on peut aussi lui donner plusieurs éléments html sous la forme d'une liste d'éléments (le premier est le children), comme ci-dessous

def create_sine_graph():
    fig, ax = plt.subplots()
    # attention, ci desssus, c'est subplots avec un s ! il va chercher la figure et les axes associés (ce qu'on voit dans la fenêtre plt(show)) et crée une nouvelle figure et ses axes, et de les donner à dashboard ; 
    # fig, ax sont deux variables mais je n'ai pas bien compris la suite (trois systèmes d'axes plutôt que trois axes ?)
    x = np.arange(0, 3*np.pi, 0.1)
    # on peut aussi utiliser np.linspace() pour donner plusieurs valeurs mais attention à la dernière : avec arange, c'est le pas ! avec linspace, je ne sais plus à vérifier
    ax.set_title("Sine Wave Form")
    # maintenant qu'on a les points (np.arange), on peut... j'ai perdu le fil (numpy est à revoir)
    ax.plot(x, np.sin(x), "r--")
    return mpl_to_plotly(fig)

app.layout = html.Div([
    html.H1("First Dash app"),
    html.H3("Bruxelles Formation 2024"),
    dcc.Slider(0, 20, 2),
    # ci dessous, on va mettre la fonction qui crée le graphique dans le dcc.Graph (à la place du dict super compliqué de la documentation en ligne)
    dcc.Graph(
    id="example-graph",
    figure=create_sine_graph()
)
])

# le pas de base de dcc.Slider est de 5. Le pas qu'on lui attribue est le dernier des trois nombres.
# le système plotly pour créer un gra^h, tel qu'il est présenté sur le site de dash, est super lourde et à éviter. On va utiliser matplotlib à la place





#la ligne suivante est pour éviter que, si je lance le dash sur un serveur de production, il ne lance la ligne app.run(debug=True), prévue pour les serveurs locaux
# le nom d'un fichier qu'on lance explicitement, c'est __main__ (à la différence des imports)

if __name__ == "__main__":
#pour lancer le petit serveyr (flask server in local mode, pour ne pas devoir installer un serveur web sur son pc)
    app.run(debug=True)
#le mode debug fait qu'il relance le truc à chaque fois qu'on modifie le fichier source



