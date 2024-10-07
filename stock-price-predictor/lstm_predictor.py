import numpy as np
from keras.models import Sequential # type: ignore
from keras.layers import LSTM, Dense # type: ignore
from utils.data_preprocessing import get_stock_data, scale_data, prepare_data
from utils.model_evaluation import evaluate_model, plot_predictions
from sklearn.model_selection import train_test_split

def run_lstm_model():
    # 1. Load and preprocess stock data
    df = get_stock_data('AAPL', '2010-01-01', '2024-01-01')
    scaled_data, scaler = scale_data(df)

    # 2. Prepare training and testing data
    X, y = prepare_data(scaled_data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # 3. Reshape data for LSTM (samples, timesteps, features)
    X_train_lstm = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    X_test_lstm = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

    # 4. Build LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train_lstm.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X_train_lstm, y_train, epochs=10, batch_size=32)

    # 5. Make predictions
    predictions_lstm = model.predict(X_test_lstm)
    predictions_rescaled = scaler.inverse_transform(predictions_lstm)

    # 6. Evaluate and plot results
    y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))
    evaluate_model(y_test_rescaled, predictions_rescaled)
    plot_predictions(y_test_rescaled, predictions_rescaled, 'LSTM Stock Price Prediction')

# Only run when executed as a script, not when imported
if __name__ == "__main__":
    run_lstm_model()
