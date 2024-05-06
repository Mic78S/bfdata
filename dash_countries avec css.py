import pandas as pd
from pathlib import Path
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from plotly.tools import mpl_to_plotly


file_path = Path(__file__).parent

df = pd.read_csv(Path(file_path, "countries.csv"), sep=",")

x = df["Literacy"]
y = df["GDPPC"]

# rajouter __name__ dans dash.Dash() pour faire le lien avec le css
app = dash.Dash(__name__)

def countries_graph(xcol="Literacy", ycol="Literacy"):
    fig, ax = plt.subplots()

    x = df[xcol]
    y = df[ycol]
    ax.scatter(x, y)

    return mpl_to_plotly(fig)


app.layout = html.Div([
    html.H1("Countries"),
    html.Div([
        dcc.Graph(figure=countries_graph(), id="country-graph"),
    ]),
    html.Div([
        dcc.RadioItems(
            options = ["Literacy", "GDPPC", "InfantMortality", "Agriculture", "Population", "NetMigration"],
            value = "Literacy", id="x-axis"),
        dcc.RadioItems(
            options = ["Literacy", "GDPPC", "InfantMortality", "Agriculture", "Population", "NetMigration"],
            value = "Literacy", id="y-axis"),
            
    ]),          
], className="border")

#par rapport au html et au css, python parle de className puisqu'il utilise le mot class pour autre chose


@app.callback(
    Output("country-graph", "figure"),
    [Input("x-axis", "value")], Input("y-axis", "value")
)

def update_countries_graph(x_column, y_column):
    return countries_graph(x_column, y_column)



if __name__ == "__main__":
    app.run(debug=True)

  