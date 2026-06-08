import pandas as pd

df = pd.read_csv("aligned_dataset.csv")

# Daily PnL
daily_pnl = (
    df.groupby("date")["value"]
    .sum()
    .reset_index()
)

print("\nDaily PnL")
print(daily_pnl.head())

# Win Rate
wins = (df["value"] > 0).sum()
total = len(df)

win_rate = (wins / total) * 100

print("\nWin Rate:", round(win_rate, 2), "%")

# Average Trade Size
avg_trade_size = df["value"].abs().mean()

print("Average Trade Size:", round(avg_trade_size, 2))

# Trades Per Day
trades_per_day = (
    df.groupby("date")
    .size()
    .reset_index(name="num_trades")
)

print("\nTrades Per Day")
print(trades_per_day.head())

# Long/Short Ratio
long_count = (
    df["classification"]
    .astype(str)
    .str.lower()
    .eq("long")
    .sum()
)

short_count = (
    df["classification"]
    .astype(str)
    .str.lower()
    .eq("short")
    .sum()
)

if short_count > 0:
    print(
        "Long/Short Ratio:",
        round(long_count / short_count, 2)
    )