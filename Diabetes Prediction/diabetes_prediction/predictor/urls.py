from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_diabetes, name='predict_diabetes'),
]
