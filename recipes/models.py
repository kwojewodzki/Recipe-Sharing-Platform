from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    amount = models.FloatField()
    unit_of_messure = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f"{self.name}: ({self.amount} {self.unit_of_messure})"
    


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.name}"