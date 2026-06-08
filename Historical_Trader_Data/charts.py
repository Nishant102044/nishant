import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("merged_data.csv")

# Chart 1
df.groupby("classification")["Closed PnL"]\
.mean().plot(kind="bar")

plt.title("Average PnL by Sentiment")
plt.show()

# Chart 2
df.groupby("classification")\
.size().plot(kind="bar")

plt.title("Trade Frequency by Sentiment")
plt.show()

# Chart 3
df.groupby("classification")["Size USD"]\
.mean().plot(kind="bar")

plt.title("Average Position Size by Sentiment")
plt.show()