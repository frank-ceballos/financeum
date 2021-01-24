# Project Description

A Python wrapper for `yahoo_finance` and `get_all_tickers`. With 
`yahoo_finance` one can easily fetch historical data for different companies 
by providing there ticker labels. However, `yahoo_finance` does not offer an
easy way to retrieve data for a large number of companies. 

To extract data for 1000s of companies you will need to scrape the web or 
compile a list manually. This problem is partially solved by `get_all_tickers`,
a Python package that allows you extract the tickers from publically
traded stocks. The stock tickers are from the NYSE, NASDAG, and AMEX. It is
important to note that NASDAQ implements anti-scraping features and as a result
`get_all_tickers` no longer works in Google Colab.

Financeum uses `get_all_tickers` to extract the ticker labels from different 
American exchanges and `yahoo_finance` to retrieve historical data for each
ticker. For each ticker provided to `yahoo_finance`, the following fields
are return:

* **Open**: The price of the first trade on the given trading day.

* **High**: The highest price at which a stock traded for the given 
  trading day.

* **Low**: The lowest price at which a stock traded for the given 
trading day.

* **Close**: The price of the final trade before the end of the 
 trading day.

* **Adj Close**: According to Yahoo Finance, this is the closing price
  after adjustments for all applicable splits and dividends
  distributions. Volume: The number of shares traded for the given
  trading day.

The compiled historical data is then saved into a csv named `stock_data.csv`.

# Installation

Install with `pip`:

```sh
pip install financeum
```

# Examples

## Fetch Data for +6000 Companies

To fetch data for +6000 companies using financeum use the following script.

```python
# Import packages
import datetime
from datetime import date, timedelta
from financeum import Financeum

# Define start and end date for the data
start_date = datetime.datetime(2017, 1, 1) # Year, Month, Day
end_date   = date.today() - timedelta(days=1)

# Initiate an instance of Financeum
financeum = Financeum(start_date, end_date)

# Get stock data
stock_data = financeum.get_data()
```

## Fetch Data Custom List of Tickers

To fetch historical financial data for Apple, Google, and Tesla use:

```python
# Import packages
import datetime
from datetime import date, timedelta
from financeum import Financeum

# Define ticker labels
ticker_labels = ['AAPL', 'GOOG', 'TSLA']

# Define start and end date for the data
start_date = datetime.datetime(2017, 1, 1) # Year, Month, Day
end_date   = date.today() - timedelta(days=1)

# Initiate an instance of Financeum
financeum = Financeum(start_date, end_date)

# Get stock data
stock_data = financeum.get_data()
```

# Contributors
* **Frank Ceballos** - [GitHub](https://github.com/frank-ceballos)