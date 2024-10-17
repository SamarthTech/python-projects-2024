
# Alzheimer's Disease Detection using Logistic Regression

This project implements a machine learning model to detect Alzheimer's disease based on patient data. Using logistic regression, the model classifies individuals as either at risk of developing Alzheimer's or not, based on various cognitive and demographic features.


## Features

- **Data Preprocessing**: Cleans and prepares the dataset for analysis.
- **Logistic Regression Model**: Utilizes logistic regression for binary classification.
- **Visualization**: Generates plots to visualize the results and model performance.
- **Web Interface**: A simple Flask-based application for user interaction.

## Technologies

This project utilizes the following libraries:

- **Flask**: A lightweight web framework for building the application.
- **NumPy**: For numerical operations.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For implementing machine learning algorithms, including logistic regression.
- **Matplotlib**: For visualizing data and model results.
- **XGBoost**: For advanced boosting techniques and feature importance analysis.
- **Boruta**: For feature selection to improve model accuracy.



### Install Dependencies

Create a virtual environment (recommended) and install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Flask Application

To start the Flask application, run the following command:

```bash
gunicorn app:app
```

The application will be available at `http://127.0.0.1:8000`.

### Making Predictions

1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. Fill in the required patient data features.
3. Click the "Submit" button to receive the prediction indicating whether the patient is at risk of Alzheimer's disease.


## Model Training

The Alzheimer's detection model is trained using a dataset that includes various cognitive and demographic features of patients. The logistic regression model is implemented using `scikit-learn`. 
