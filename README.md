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
├── src/
│   ├── backtest.py
│   └── analysis.py
├── .gitignore
├── README.md
├── requirements.txt
└── .gitattributes
```

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

