
# Ganymede - Trading Data Analysis

## Project Introduction

This project was developed as part of a technical test for Ganymede.

The objective is to build a small Python application to control and analyze anonymized trading data.

The analysis focuses on key trading performance metrics, including:

- Number of trades
- Win rate
- Total and average PnL
- Profit Factor
- Maximum Drawdown
- Average result in R
- LONG / SHORT analysis
- Analysis by instrument
- Maximum Adverse Excursion (MAE)
- Cumulative PnL
- Drawdown

The project also provides visualizations of cumulative PnL and drawdown.
## Project Structure
test-1-ganymede/
│
├── data/
│   └── GANYMEDE_Test_Trading_Data_Anonymise.csv
│
├── src/
│   ├── backtest.py
│   └── analysis.py
│
├── README.md
└── requirements.txt

# Requirmwnts
The project requires:
Python 3.10+
Pandas
NumPy
Matplotlib
 to install dependencies :pip install -r requirements.txt
## Notes

The dataset file is intentionally ignored by Git so it does not get committed to version control.

## Run
 1-Clone the repository:
git clone YOUR_GITHUB_REPOSITORY_URL
 2-Navigate to the project
cd test-1-ganymede
 3-Install the dependencies
 pip install -r requirements.txt
  4-Run the analysis:
  python src/analysis.py
  



