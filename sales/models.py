from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    qty = models.IntegerField()
    tax = models.FloatField()
    total = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)