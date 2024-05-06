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

x = df.corr(["Literacy"])
y = df.corr(["GDPPC"])

plt.scatter(df.corr(["Literacy"]), df.corr(["GDPPC"]))


# coeff = np.polyfit(df["Literacy"], df["GDPPC"], 1)


plt.plot(x, y, "ro")
plt.show()