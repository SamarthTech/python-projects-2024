from django.contrib import admin
from .models import Restaurants,TrainingData,MoodData
# Register your models here.
admin.site.register(Restaurants)
admin.site.register(TrainingData)
admin.site.register(MoodData)
