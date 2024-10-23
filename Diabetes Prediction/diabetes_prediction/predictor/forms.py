from django import forms

class PredictionForm(forms.Form):
    pregnancies = forms.IntegerField(label='Pregnancies')
    glucose = forms.FloatField(label='Glucose Level')
    blood_pressure = forms.FloatField(label='Blood Pressure')
    skin_thickness = forms.FloatField(label='Skin Thickness')
    insulin = forms.FloatField(label='Insulin Level')
    bmi = forms.FloatField(label='BMI')
    dpf = forms.FloatField(label='Diabetes Pedigree Function')
    age = forms.IntegerField(label='Age')
