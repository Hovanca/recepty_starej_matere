from django.db import models
from .forms import DifficultyForm

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length = 50)
    grams = models.IntegerField()

    def __str__(self):
        return self.name

class Recept(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    #thumbnail
    cooking_time = models.DurationField()
    #https://www.geeksforgeeks.org/durationfield-django-models/ toto niekde musis pridat
    #https://pytutorial.com/django-durationField-examples
    portions = models.IntegerField()
    #difficulty = DifficultyForm()
    #mozno to je zle https://www.geeksforgeeks.org/choicefield-django-forms/
    #ingredients = Ingredients()


    def __str__(self):
        return self.name
