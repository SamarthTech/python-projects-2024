from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"



MOOD_CHOICES= [
    ('Happie', 'Happie'),
    ('Angrie', 'Angrie'),
    ('Dehydratie', 'Dehydratie'),
    ('Depressie', 'Depressie'),
    ('Excitie', 'Excitie'),
    ('Unwellie', 'Unwellie'),
    ]
RESTAURANT_CHOICES=[
   (1,'PizzaHut'),(2,'Dominos'),(3,'BeijingStreet'),(4,'KakeDiHatti'),(5,'ItalianJoint'),(6,'ChineseYum'),(7,'SagarRatna'),(8,'QDs'),(9,'DCafe'),(10,'Tamasha'),(11,'MasalaTrail'),
]

FOOD_CHOICES=[
   (1,'Cholle Bhature'),(2,'Rajma Chawal'),(3,'Pasta'),(4,'Garlic Bread'),(5,'Ham'),(6,'Spring Roll'),(7,'Idli'),(8,'Dosa'),(9,'Noodles'),(10,'Chilly Paneer'),(11,'Vada pao'),(12,'Aaloo Tikki'),(13,'Tea'),(14,'Ice Cream'),(15,'Chocolates'),(16,'Pastries'),(17,'Juices'),(18,'Soft Drinks')
]

class Feedback(forms.Form):

    Restaurant=forms.CharField(widget=forms.Select(choices=RESTAURANT_CHOICES))
    Food=forms.CharField(widget=forms.Select(choices=FOOD_CHOICES))
    Mood= forms.CharField(label='How are you feeling today?', widget=forms.Select(choices=MOOD_CHOICES))
    Rating=forms.DecimalField(label='Rating(On a scale of 5)', max_value=5, min_value=0)
