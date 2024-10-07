import yfinance as yf
import numpy as np

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_stock_data(ticker, start_date, end_date):
    """
    Downloads stock data for a given ticker symbol.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def scale_data(df):
    """
    Scales the data using MinMaxScaler.
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df[['Close']])
    return scaled_data, scaler

def prepare_data(data, window_size=60):
    """
    Prepares data for training by creating windows of previous days.
    """
    X, y = [], []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i, 0])
        y.append(data[i, 0])
    return np.array(X), np.array(y)
