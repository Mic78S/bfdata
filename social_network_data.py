import pandas as pd
import matplotlib as plt

folder = Path(__file__).parent
file = Path(folder, "social_network_data.csv")

df = pd.read_csv(file)

print(df["friends"].value_counts())


plt.plot(df["friends"])
plt.show()

