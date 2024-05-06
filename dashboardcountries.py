from pickle import OBJ
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from plotly.tools import mpl_to_plotly

file_path = Path(__file__).parent

df = pd.read_csv(Path(file_path, "countries.csv"))

x = df.corr(["Literacy"])
y = df.corr(["GDPPC"])

plt.scatter(df.corr(["Literacy"]), df.corr(["GDPPC"]))


# coeff = np.polyfit(df["Literacy"], df["GDPPC"], 1)


plt.plot(x, y, )
plt.show()


app = dash.Dash()

def countries_graph(func):
    fig, ax = plt.subplots()
    x = df.corr(["Literacy"])
    
    ax.set_title("Literacy and GDPPC")
    ax.plot(x, y, "ro")
    return mpl_to_plotly(fig)

app.layout = html.Div([
    html.H1("Literacy and GDPPC"),
    dcc.Graph(figure=countries_graph(), id="country-graph")
])

#app.callback(Output("sine-graph", "figure"), [Input("graph-slider", "value")])


# def update_sine_graph(slider_value):
  #  return create_sine_graph(slider_value)


if __name__ == "__main__":
  app.run(debug=True)

#plt.xlabel("Pays")
#plt.ylabel("Taux d'alphabétisation")
#plt.plot(x, y)
#plt.show()