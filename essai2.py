#from pickle import OBJ
import pandas as pd
from pathlib import Path
#import numpy as np
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

#plt.scatter(df["Literacy"], df["GDPPC"])


# coeff = np.polyfit(df["Literacy"], df["GDPPC"], 1)


#plt.plot(x, y, "ro")


app = dash.Dash()

def countries_graph(xcol="Literacy", ycol="GDPPC"):
    fig, ax = plt.subplots()
    x = df["Literacy"]
    y = df["GDPPC"]
    #ax.set_title("Literacy and GDPPC")
    ax.scatter(x, y)
    return mpl_to_plotly(fig)

app.layout = html.Div([
    html.H1("Countries"),
    dcc.Graph(figure=countries_graph(), id="country-graph"),
    dcc.RadioItems(
      options = ["Literacy", "GDPPC", "InfantMortality","Agriculture","Population", "NetMigration"],
        value = "Literacy", id="x-axis")
])


@app.callback(Output("country-graph", "figure"), [Input("x-axis", "value")])


def update_countries_graph(x_column):
    return countries_graph(x_column)


if __name__ == "__main__":
  app.run(debug=True)
