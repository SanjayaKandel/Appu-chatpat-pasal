from django.db import models

# Create your models here.

""" 
Model OF items and drinks
"""
class Items(models.Model):
    image = models.ImageField(upload_to='static/image/', null=True, blank=True)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Drinks(models.Model):
    image = models.ImageField(upload_to='static/image/', null=True, blank=True)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
