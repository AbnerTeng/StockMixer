import pandas as pd


df = pd.read_csv("sp500_ticker.csv")
groups = df.groupby("Sector")
print(len(groups))
