![Drag Racing](Assets/logo.jpeg)

# Project Description

Financeum is a simple to use package for collecing large amounts of historical
financial data.

Provides:

  1. An easy way to collect and download historical financial data for 1000s 
  of companies.

Financeum is a Python wrapper that is built on top of `yahoo_finance` and
`get_all_tickers`.  Financeum uses `get_all_tickers` to extract the ticker
labels from different American exchanges and `yahoo_finance` to retrieve 
historical data for each ticker. For each ticker provided to `yahoo_finance`, 
the following fields are return:

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

The compiled historical data is then return as a pandas dataframe and saved 
into a csv file named `stock_data.csv`.


# Installation

Install with `pip`:

```sh
pip install financeum
```

# Documentation

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

In the above script, the `start_date` and `end_date` are `datetime.datetime` 
objects and are required parameters. After the data is downloaded is saved
into a csv file and pandas dataframe is returned. The indices of the pandas
dataframe are the dates. 

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
financeum = Financeum(start_date, end_date, ticker_labels=ticker_labels)

# Get stock data
stock_data = financeum.get_data()
```

There is nothing special here, we are simply using the `yahoo_finance` in the
backend to do this.

Here are the first few columns of `stock_data`

```
Date         AAPL Adj Close  AAPL Close  AAPL High   AAPL Low   AAPL Open  AAPL Volume 
2017-01-03   27.500973       29.037500    29.082500  28.690001  28.950001  1151276000      
2017-01-04   27.470192       29.004999    29.127501  28.937500  28.962500  84472400     
2017-01-05   27.609884       29.152500    29.215000  28.952499  28.980000  887744000      
2017-01-06   27.917688       29.477501    29.540001  29.117500  29.195000  1270076000      
```

# License
[MIT](LICENSES/MIT.txt)

# Contributors
* **Frank Ceballos** - [GitHub](https://github.com/frank-ceballos)