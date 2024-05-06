import dash
# pour éviter de taper dash.import à chaque fois (rappel)
from dash import html
#on crée une instance de la classe Dash
app = dash.Dash()
#on lui donne un layout minimum (ici, un Div), parce que dash en a besoin
# on peut mettre du texte dans le Div, mais on peut aussi mettre du html et du cass
#app.layout = html.Div("Hello everyone !")
#app.layout = html.Div(html.H1("First Dash app"))
#on peut aussi lui donner plusieurs éléments html sous la forme d'une liste d'éléments (le premier est le children), comme ci-dessous
app.layout = html.Div([
    html.H1("First Dash app"),
    html.H3("Bruxelles Formation 2024")
])


#la ligne suivante est pour éviter que, si je lance le dash sur un serveur de production, il ne lance la ligne app.run(debug=True), prévue pour les serveurs locaux
# le nom d'un fichier qu'on lance explicitement, c'est __main__ (à la différence des imports)

if __name__ == "__main__":
#pour lancer le petit serveyr (flask server in local mode, pour ne pas devoir installer un serveur web sur son pc)
    app.run(debug=True)
#le mode debug fait qu'il relance le truc à chaque fois qu'on modifie le fichier source



