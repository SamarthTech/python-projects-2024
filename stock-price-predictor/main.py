import sys
from decision_tree_predictor import run_decision_tree_model
from lstm_predictor import run_lstm_model

def main():
    print("Stock Price Predictor")
    print("Choose a model to run:")
    print("1. Decision Tree Model")
    print("2. LSTM Model")

    choice = input("Enter 1 or 2: ")

    if choice == '1':
        print("\nRunning Decision Tree Model...")
        run_decision_tree_model()
    elif choice == '2':
        print("\nRunning LSTM Model...")
        run_lstm_model()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit()

if __name__ == "__main__":
    main()
