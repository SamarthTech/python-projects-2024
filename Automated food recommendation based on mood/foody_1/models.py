from django.db import models

# Create your models here.
class Restaurants(models.Model):
    name=models.CharField(max_length=256)
    latitude=models.DecimalField(max_digits=6,decimal_places=2)
    longitude=models.DecimalField(max_digits=6,decimal_places=2)
    rating=models.DecimalField(max_digits=6,decimal_places=2)
    cost=models.IntegerField()
    count=models.IntegerField()
    chholebature=models.IntegerField()
    rajmachawal=models.IntegerField()
    dosa=models.IntegerField()
    idli=models.IntegerField()
    noodles=models.IntegerField()
    chillypaneer=models.IntegerField()
    alootikki=models.IntegerField()
    vadapao=models.IntegerField()
    garlicbread=models.IntegerField()
    pasta=models.IntegerField()
    springroll=models.IntegerField()
    ham=models.IntegerField()
    icecream=models.IntegerField()
    pastries=models.IntegerField()
    chocolates=models.IntegerField()
    tea=models.IntegerField()
    softdrinks=models.IntegerField()
    juices=models.IntegerField()


class TrainingData(models.Model):
    rating=models.DecimalField(max_digits=6,decimal_places=2)
    distance=models.IntegerField()
    cost=models.IntegerField()
    yesno=models.IntegerField()


class MoodData(models.Model):
    Dish=models.CharField(max_length=50)
    happie=models.IntegerField()
    angrie=models.IntegerField()
    dehydratie=models.IntegerField()
    depressie=models.IntegerField()
    excitie=models.IntegerField()
    unwellie=models.IntegerField()
