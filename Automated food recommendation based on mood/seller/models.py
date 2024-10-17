from django.db import models

class Seller(models.Model):
    Name=models.CharField(max_length=264)
    Address=models.CharField(max_length=264)
    Items=models.CharField(max_length=264)
