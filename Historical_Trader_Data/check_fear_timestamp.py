import pandas as pd

fear = pd.read_excel("fear_greed_index.xlsx")

print(fear.head())
print("\nTimestamp Values:")
print(fear["timestamp"].head(10))
print("\nData Type:")
print(fear["timestamp"].dtype)