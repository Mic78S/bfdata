from pickle import OBJ
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib
#matplotlib.use("agg")
import matplotlib.pyplot as plt
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from plotly.tools import mpl_to_plotly

file_path = Path(__file__).parent

df = pd.read_csv(Path(file_path, "countries.csv"))

x = df["Literacy"]
y = df["GDPPC"]

plt.scatter(df["Literacy"], df["GDPPC"])


# coeff = np.polyfit(df["Literacy"], df["GDPPC"], 1)


plt.plot(x, y, "ro")


app = dash.Dash()

def countries_graph():
    fig, ax = plt.subplots()
    x = np.linspace(0, 100000, 100000)
    ax.set_title("Literacy and GDPPC")
    ax.plot(x, np.sin(x), "ro")
    return mpl_to_plotly(fig)

app.layout = html.Div([
    html.H1("Countries"),
    dcc.Graph(figure=countries_graph(), id="country-graph")
])

#app.callback(Output("sine-graph", "figure"), [Input("graph-slider", "value")])


# def update_sine_graph(slider_value):
  #  return create_sine_graph(slider_value)


if __name__ == "__main__":
  app.run(debug=True)
