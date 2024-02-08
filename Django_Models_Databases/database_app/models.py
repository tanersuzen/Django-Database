from django.db import models

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=40)
    instrument = models.CharField(max_length=30)
    age = models.IntegerField()