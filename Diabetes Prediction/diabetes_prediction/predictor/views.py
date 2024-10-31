from django.shortcuts import render
from .forms import PredictionForm
import joblib
import numpy as np

# Load the saved model
model = joblib.load('diabetes_model.pkl')

def predict_diabetes(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get the form data
            pregnancies = form.cleaned_data['pregnancies']
            glucose = form.cleaned_data['glucose']
            blood_pressure = form.cleaned_data['blood_pressure']
            skin_thickness = form.cleaned_data['skin_thickness']
            insulin = form.cleaned_data['insulin']
            bmi = form.cleaned_data['bmi']
            dpf = form.cleaned_data['dpf']
            age = form.cleaned_data['age']

            # Convert form data into an array
            input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

            # Make the prediction
            prediction = model.predict(input_data)

            result = 'Diabetic' if prediction[0] == 1 else 'Not Diabetic'

            return render(request, 'result.html', {'result': result})

    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form})
