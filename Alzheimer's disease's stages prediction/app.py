import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

# Load the scaler
fp = open("scaler.bin", "rb")
scaler = pickle.load(fp)
fp.close()

# Load LinearSVM
fp = open("LinearSVM.bin", "rb")
model1 = pickle.load(fp)
fp.close()

# Load LogisticRegression
fp = open("LogisticRegression.bin", "rb")
model2 = pickle.load(fp)
fp.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [[float(x) for x in request.form.values()]]
    final_features = scaler.transform(int_features)
    #output = model.predict(final_features)
    # Now convert linear svm's prediction to probability
    out1 = sigmoid(model1.decision_function(final_features))
    # Get prediction probability from logistic regression
    out2 = model2.predict_proba(final_features)[:,1]

    # Their average is the final output probability
    final_output = np.mean((out1, out2), axis=0)
    #output = prediction.reshape(-1, 1)
    output=(str(round(final_output[0]*100, 2)))
    return render_template('index.html', prediction_text='Chance of alzheimer disease {}%'.format(output))


if __name__ == "__main__":
    app.run(debug=True)