import pandas as pd


df = pd.read_csv("data/ont.csv")

print(df)

water_level = df.iloc[1]

years = df.loc["years"]

plt.plot(years, water_level)