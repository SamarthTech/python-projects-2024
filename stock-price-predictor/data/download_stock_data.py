import yfinance as yf
import pandas as pd

def download_stock_data(ticker, start_date, end_date, filename='stock_data.csv'):
    """
    Downloads historical stock data from Yahoo Finance and saves it to a CSV file.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple).
        start_date (str): Start date for historical data (format: 'YYYY-MM-DD').
        end_date (str): End date for historical data (format: 'YYYY-MM-DD').
        filename (str): Name of the CSV file where the data will be saved.
    """
    # Download stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Save data to CSV with the correct filename
    stock_data.to_csv(filename)
    print(f"Data saved to {filename}")

# Example usage
if __name__ == "__main__":
    download_stock_data('AAPL', '2010-01-01', '2024-01-01')
