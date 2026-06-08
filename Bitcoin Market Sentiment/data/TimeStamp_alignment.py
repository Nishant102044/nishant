import pandas as pd

df = pd.read_excel("fear_greed_index.xlsx")

df.columns = df.columns.str.strip()

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df["date"] = df["timestamp"].dt.date

print(df[["timestamp", "date"]].head())

df.to_csv(
    "aligned_dataset.csv",
    index=False
)

print("Dataset aligned and saved.")