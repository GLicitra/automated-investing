import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

desired_width = 100
pd.set_option("display.width", desired_width)
pd.set_option("display.max_columns", 10)

np.random.seed(seed=42)

# define StopOrder policy
df_StopOder = pd.DataFrame(
    data={
        "stock-min": [0, 20, 50, 200],
        "stock-max": [20, 50, 200, np.inf],
        "stop-order": [0.01, 0.01, 0.5, 1],
        "unit": ["%", "%", "absolute", "absolute"],
        "currency": 4 * ["dollar"],
    }
)

# span for Exponential Moving Average (EMA)
windowEMA = {"ema9": 9, "ema16": 16, "ema65": 65, "ema200": 200}

# =========================================
# creat pseudo stocks

list_stocks = ["AAPL", "BABA", "FB", "NFLX"]

df_stocks = pd.DataFrame(
    np.random.randn(289, len(list_stocks)),
    index=pd.date_range(start="2014/01/04", end="2014/01/05", freq="5min"),
    columns=list_stocks,
).cumsum()  # generate random-walk

# =======================================
df_ema = pd.DataFrame(data=0 * [df_stocks.shape[0]], index=df_stocks.index)
for key, value in windowEMA.items():
    # calculate EMA with value span, adjust name and merge
    temp = df_stocks.ewm(span=value, adjust=False).mean()
    _ = temp.rename(
        columns=dict(zip(temp.columns, temp.columns + "_" + key)),
        errors="raise",
        inplace=True,
    )
    df_ema = df_ema.merge(right=temp, how="left", left_index=True, right_index=True)

# merge to the original dataframe
df_stocks = df_stocks.merge(right=df_ema, how="left", left_index=True, right_index=True)

# =======================================
# Plot
fig, axs = plt.subplots(2, 2, figsize=(15, 6), facecolor="w", edgecolor="k")
fig.subplots_adjust(hspace=0.5, wspace=0.001)
axs = axs.ravel()

for i, stock in zip(range(len(list_stocks)), list_stocks):
    print(i, "->", stock)
    _ = df_stocks.filter(regex=stock).plot(ax=axs[i])
    axs[i].set_title(stock)

plt.show()
