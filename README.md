# Getting Started

A Python wrapper for `yahoo_finance` and `get_all_tickers`. Using 
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
