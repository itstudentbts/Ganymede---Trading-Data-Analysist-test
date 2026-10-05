import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\HP\Downloads\GANYMEDE_Test_Trading_Data_Anonymise.csv',               
    sep=";",
    parse_dates=["entry_time_utc", "exit_time_utc"],
)
number_of_trades = len(df)
print(f"Number of trades: {number_of_trades}")
win_rate = (df["net_pnl_usd"] > 0).mean() * 100
print(f"Win rate: {win_rate:.2f}%")
total_pnl = df["net_pnl_usd"].sum()
print(f"Total P&L: {total_pnl:.2f}")
average_pnl = df["net_pnl_usd"].mean()
print(f"Average P&L per trade: {average_pnl:.2f}")
#$Profit Factor
gross_profit = df.loc[df["net_pnl_usd"] > 0, "net_pnl_usd"].sum()
gross_loss = -df.loc[df["net_pnl_usd"] < 0, "net_pnl_usd"].sum()
profit_factor = gross_profit / gross_loss
print(f"Profit Factor: {profit_factor:.2f}")
#$Cumulative PnL
df["entry_time_utc"] = pd.to_datetime(df["entry_time_utc"], utc=True)
df = df.sort_values("entry_time_utc").reset_index(drop=True)
df["cumulative_pnl"] = df["net_pnl_usd"].cumsum()
print(f"Cumulative P&L: {df['cumulative_pnl'].iloc[-1]:.2f}")
#$Maximum Drawdown
df["peak_pnl"] = df["cumulative_pnl"].cummax()
df["drawdown"] = df["cumulative_pnl"] - df["peak_pnl"]
max_drawdown = df["drawdown"].min()
print(f"Maximum Drawdown: {max_drawdown:.2f}")
#$LONG / SHORT analysis
long_trades = df[df["side"] == "LONG"]
short_trades = df[df["side"] == "SHORT"]
long_pnl = long_trades["net_pnl_usd"].sum()
short_pnl = short_trades["net_pnl_usd"].sum()
long_win_rate = (long_trades["net_pnl_usd"] > 0).mean() * 100
short_win_rate = (short_trades["net_pnl_usd"] > 0).mean() * 100
print(f"LONG Win Rate: {long_win_rate:.2f}%")
print(f"SHORT Win Rate: {short_win_rate:.2f}%")
short_avg_pnl = (short_trades["net_pnl_usd"] > 0).mean()
print(f"SHORT Average P&L: {short_avg_pnl:.2f}%")
#$Analysis by instrument
instrument_analysis = df.groupby("instrument").agg(
    trades=("trade_id", "count"),
    total_pnl=("net_pnl_usd", "sum"),
    win_rate=("net_pnl_usd", lambda x: (x > 0).mean() * 100),
    average_pnl=("net_pnl_usd", "mean"),
    average_r=("net_r", "mean")
)
print("\nAnalysis by instrument:")
print(instrument_analysis)
#$Maximum Adverse Excursion Analisis
df["mae_usd"].describe()
worst_mae = df.nlargest(5, "mae_usd")
print(f"Maximum Adverse Excursion: {worst_mae['mae_usd'].max():.2f}")
#GRAPH
plt.plot(df["entry_time_utc"], df["cumulative_pnl"])
plt.plot(df["entry_time_utc"], df["drawdown"])
plt.xlabel("Time")
plt.ylabel("P&L")
plt.title("Cumulative P&L and Drawdown")
plt.legend(["Cumulative P&L", "Drawdown"])
plt.show()
