""" ***************************************************************************
# * File Description:                                                         *
# *                                                                           *
# * Class used to retrieve historical financial data for US companies.        *
# *                                                                           *
# * --------------------------------------------------------------------------*
# * AUTHORS(S): Frank Ceballos <frank.ceballos123@gmail.com>                  *
# *           : David Sicilian                                                *
# * --------------------------------------------------------------------------*
# * DATE CREATED: January 21, 2021                                            *
# * LAST UPDATE : ----                                                        *
# * --------------------------------------------------------------------------*
# * NOTES:                                                                    *
# * ************************************************************************"""


# To manipulate data
import pandas as pd

# To grab a list of tickers
from get_all_tickers import get_tickers as gt

# To grab stock data
import yfinance as fyf
from pandas_datareader import data as pdr
fyf.pdr_override() # <-- Here is the fix


class Financeum:
    """
    The Financeum class is use to collect historical data from US Markets. 
    Given a list of tickers, for each ticker in the list extract the historical 
    data containing the following fields from Yahoo Finance:
    
        Open: The price of the first trade on the given trading day.
        
        High: The highest price at which a stock traded for the given 
        trading day.
        
        Low: The lowest price at which a stock traded for the given 
        trading day.
        
        Close: The price of the final trade before the end of the 
        trading day.
        
        Adj Close: According to Yahoo Finance, this is the closing price
        after adjustments for all applicable splits and dividends
        distributions. Volume: The number of shares traded for the given
        trading day.
        
    Ticker labels for which no data can be found will discarded. When a list
    of tickers is not provided by the user, +68000 tickers are used to extract
    historical data from US markets. The historical data is then dumped into a
    csv file. 
                
    
    Parameters
    ----------
    
    start_date: datetime.datetime
        The start date for the dataset
        
    end_date: datetime.datetime
        The end date for the dataset
        
    ticker_labels: list, optional
        A list containing the ticker labels. The default values is over +6000
        tickers from the US market.
        
  
    Example
    -------
    
    # Import packages
    import datetime
    from datetime import date, timedelta
    
    # Define start and end date for the data
    start_date = datetime.datetime(2017, 1, 1) # Year, Month, Day
    end_date   = date.today() - timedelta(days=1)
    
    # Initiate an instance of Financeum
    financeum = Financeum(start_date, end_date)
    
    # Get stock data
    financeum.get_data()
    
    
    Attributes
    ----------
    
    None
    
    Author Information
    ------------------
    
    Frank Ceballos
    LinkedIn: <https://www.linkedin.com/in/frank-ceballos/>
    Date: January 22, 2021
    """
    
    
    def __init__(self, start_date, end_date, ticker_labels = None):
        
        self.start_date = start_date
        self.end_date = end_date
        self.ticker_labels = gt.get_tickers() if ticker_labels is None else ticker_labels
    
    
    def get_data(self):
        """
        get_data() is used to grab historical data from Yahoo Finance. After 
        fetching the data for the provided tickers, a file is saved under
        the current working directory under the name 'stock_data.csv'
                    
        
        Parameters
        ----------
        
        file_name: str
            The start date for the dataset
          
        
        Returns
        -------
        A pandas dataframe with the historical data for each ticker.

        """
        
        
        # Get the number of tickers
        num_tickers = len(self.ticker_labels)
        
        # All indices
        indices = list(self.chunks(list(range(num_tickers)), 1500))
        
        for subset in indices:  
            
            # Set start and end dates
            start = self.start_date
            end  = self.end_date
            
            # Subset of ticker labels
            sub_tickers = [self.ticker_labels[ii] for ii in subset]
            
            # Grab data
            data = pdr.get_data_yahoo(sub_tickers, start = start, end = end)
            
            # Decompose data
            values = data.values
            dates = data.index
            
            # Get columns labels
            columns = data.columns.tolist()
            columns = [column[1] + ' ' + column[0] for column in columns]
            
            # Create new temp dataframe
            df_temp = pd.DataFrame(values, columns = columns, index = dates)
            
            # Save to a dataframe
            if 0 in subset:
                stock_data = df_temp
            else:
                stock_data = pd.concat([stock_data, df_temp], axis = 1)

        # Remove repeated columns
        stock_data = stock_data.loc[:, ~stock_data.columns.duplicated()]
        
        # Rearrange columns alphabetically
        stock_data = stock_data.sort_index(axis=1)

        # Save file
        stock_data.to_csv('stock_data.csv')
        
        return stock_data
    
    
    def chunks(self, lst, n):
        """Yield successive n-sized chunks from list."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]