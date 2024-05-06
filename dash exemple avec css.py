import dash
from dash import html, dcc
from plotly.tools import mpl_to_plotly
import matplotlib.pyplot as plt
import numpy as np

app = dash.Dash()

def create_sine_graph():
    fig, ax = plt.subplots()
    x = np.arange(0, 3*np.pi, 0.1)
    ax.set_title("Sine Wave Form")
    ax.plot(x, np.sin(x), "r--")
    return mpl_to_plotly(fig)

app.layout = html.Div([
    html.H1("First Dash app"),
    html.H3("Bruxelles Formation 2024"),
    dcc.Slider(0, 20, 2),
    dcc.Graph(
    id="example-graph",
    figure=create_sine_graph()
)
])


if __name__ == "__main__":
    app.run(debug=True)



