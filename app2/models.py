from django.db import models

# Create your models here.

class Country(models.Model):
    country_name=models.CharField(max_length=100,primary_key=True)
    
class Captials(models.Model):
    Captial_name=models.ForeignKey(Country,max_length=100,on_delete=models.CASCADE)
