import pandas as pd

df = pd.read_csv("merged_data.csv")

print("\nTrade Frequency")
print(
    df.groupby("classification")
    .size()
)

print("\nAverage Position Size")
print(
    df.groupby("classification")["Size USD"]
    .mean()
)

print("\nLong / Short Bias")
print(
    pd.crosstab(
        df["classification"],
        df["Direction"]
    )
)