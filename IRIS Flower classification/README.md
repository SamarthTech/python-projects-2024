# IRIS Flower classification (Flask)

This project implements an Iris Flower Classification model using machine learning techniques. The model predicts the species of an iris flower based on various features such as sepal length, sepal width, petal length, and petal width.

## Features

- Predicts the species of iris flowers: Setosa, Versicolor, or Virginica.
- Visualizes data and model performance using Seaborn and Matplotlib.
- User-friendly interface for model input and output using Flask.

## Technologies

This project uses the following libraries:

- **Flask**: A lightweight web framework for building the web application.
- **Flask-WTF**: Provides integration with WTForms for handling forms.
- **NumPy**: For numerical computations.
- **Pandas**: For data manipulation and analysis.
- **Seaborn**: For statistical data visualization.
- **Matplotlib**: For creating static, animated, and interactive visualizations.
- **Scikit-learn**: For implementing machine learning algorithms.
- **Joblib**: For saving and loading models.

## Installation

### Prerequisites

Make sure you have Python 3.6+ installed. You can download it from [python.org](https://www.python.org/downloads/).

### Install Dependencies

Create a virtual environment (recommended) and install the required libraries:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Flask Application

To start the Flask application, run the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

### Making Predictions

1. Open your web browser and go to `http://127.0.0.1:5000`.
2. Enter the features of the iris flower (sepal length, sepal width, petal length, petal width) into the form.
3. Click the "Submit" button to receive the predicted species.

## Project Structure

```
├── app.py                  # Flask application file
├── requirements.txt         # List of dependencies
├── model.py                 # Model training and prediction logic
├── forms.py                 # Form definitions using Flask-WTF
├── static/                  # Static files (CSS, JS)
└── templates/               # HTML templates for the web interface
```
