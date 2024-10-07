import numpy as np
from sklearn.tree import DecisionTreeRegressor
from utils.data_preprocessing import get_stock_data, scale_data, prepare_data
from utils.model_evaluation import evaluate_model, plot_predictions
from sklearn.model_selection import train_test_split

def run_decision_tree_model():
    # 1. Load and preprocess stock data
    df = get_stock_data('AAPL', '2010-01-01', '2024-01-01')
    scaled_data, scaler = scale_data(df)

    # 2. Prepare training and testing data
    X, y = prepare_data(scaled_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # 3. Train Decision Tree model
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)

    # 4. Make predictions
    predictions = model.predict(X_test)
    predictions_rescaled = scaler.inverse_transform(predictions.reshape(-1, 1))

    # 5. Evaluate and plot results
    y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))
    evaluate_model(y_test_rescaled, predictions_rescaled)
    plot_predictions(y_test_rescaled, predictions_rescaled, 'Decision Tree Stock Price Prediction')

# Only run when executed as a script, not when imported
if __name__ == "__main__":
    run_decision_tree_model()
