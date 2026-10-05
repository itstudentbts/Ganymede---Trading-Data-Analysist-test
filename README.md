# Ganymede - Trading Data Analysis

## Project Introduction

This project was developed as part of a technical test for Ganymede.

The objective is to build a small Python application to analyze anonymized trading data and evaluate trading performance.

The analysis focuses on key metrics such as:

- Number of trades
- Win rate
- Total and average PnL
- Profit factor
- Maximum drawdown
- Average result in R
- LONG / SHORT analysis
- Analysis by instrument
- Maximum adverse excursion (MAE)
- Cumulative PnL
- Drawdown

The project also includes visualizations of cumulative PnL and drawdown.

## Project Structure

```text
Ganymede---Trading-Data-Analysist-test/
├── data/
│   └── GANYMEDE_Test_Trading_Data_Anonymise.csv
├── image/
│   └── cumulativeand drawdown.png
├── src/
│   ├── backtest.py
│   └── analysis.py
├── .gitignore
├── README.md
├── requirements.txt
└── .gitattributes
```

## Results Visualization

The cumulative P&L and drawdown chart below summarizes the strategy performance over time:

![Cumulative P&L and Drawdown](image/cumulativeand%20drawdown.png)

## Requirements

The project requires:

- Python 3.10+
- Pandas
- NumPy
- Matplotlib

To install dependencies:

```bash
pip install -r requirements.txt
```

## Notes

The anonymized dataset is intentionally ignored by Git so it is not committed to version control.

## Run

1. Clone the repository:

```bash
git clone https://github.com/itstudentbts/Ganymede---Trading-Data-Analysist-test.git
```

2. Navigate to the project folder:

```bash
cd Ganymede---Trading-Data-Analysist-test
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the analysis:

```bash
python src/analysis.py
```

5. Results:

The strategy generated 18 trades during the analyzed period, with an overall win rate of 83.33%. However, despite the relatively high proportion of profitable trades, the strategy ended the period with a negative total P&L of -323.40 USD and an average loss of -17.97 USD per trade. The profit factor was 0.89, indicating that gross losses exceeded gross gains, and the maximum drawdown reached -2304.50 USD.

Key performance indicators:
- Total trades: 18
- Win rate: 83.33%
- Total P&L: -323.40 USD
- Average P&L per trade: -17.97 USD
- Profit factor: 0.89
- Cumulative P&L: -323.40 USD
- Maximum drawdown:  2,304.50 USD 

Directional performance:
- Long trades: 85.71% win rate
- Short trades: 75.00% win rate
- Short-side average P&L: 0.75%

Instrument breakdown:
- MGC 12-26: 4 trades, average R = 0.1428
- MNQ 12-26: 14 trades, average R = -0.0706

Risk metrics:
- Maximum adverse excursion (MAE): -2.50 USD