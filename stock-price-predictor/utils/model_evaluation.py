import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

def evaluate_model(actual, predicted):
    """
    Evaluates the model performance using Mean Squared Error.
    """
    mse = mean_squared_error(actual, predicted)
    print(f"Mean Squared Error: {mse}")
    return mse

def plot_predictions(actual, predicted, title):
    """
    Plots the actual vs predicted stock prices.
    """
    plt.plot(actual, color='blue', label='Actual Stock Price')
    plt.plot(predicted, color='red', label='Predicted Stock Price')
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
