import csv
import pandas as pd

df = pd.read_csv("Bitcoin Historical Data.csv")
print(df.head())

columns1 = ["Price", "Open", "High", "Low"]

for col in columns1:
    df[col] = (
        df[col]
        .str.replace(",","",regex=False)
        .astype(float)
    )
df["Change %"] = (
    df["Change %"]
    .str.replace("%","",regex=False)
    .astype(float)
    / 100
)
def convert_volume(value):
    if "K" in value:
        return float(value.replace("K", "")) * 1000
    elif "M" in value:
        return float(value.replace("M", "")) * 1000000
    elif "B" in value:
        return float(value.replace("B", "")) * 1000000000
    else:
        return float(value)
df["Vol."] = df["Vol."].apply(convert_volume)

print(df.head())