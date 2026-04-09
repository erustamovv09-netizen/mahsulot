from django.db import models

# Create your models here.
class Mahsulot(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField()
    brand = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    transmission = models.CharField()
    engine_volume = models.CharField()
    year = models.IntegerField()
    fuel_type = models.CharField()
    image = models.CharField()