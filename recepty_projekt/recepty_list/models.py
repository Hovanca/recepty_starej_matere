from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length = 50)
    grams = models.IntegerField()

    def __str__(self):
        return self.name+ ' ' +str(self.grams)


#tu sa nam to ukaze ako v administracii
class Recept(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    thumbnail = models.ImageField(upload_to = "recepty/", blank = True)
    cooking_time = models.DurationField()
    portions = models.IntegerField()

    DIFFICULTY_CHOICES = [
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'Hard'),
    ]
    difficulty = models.CharField(max_length = 1, choices = DIFFICULTY_CHOICES, default = '1')
    ingredients = models.ManyToManyField(Ingredient, blank = True , related_name = "Ingredient")

    #pouziva sa many to many aby tie ingredience sa nevymazavali
    #alternativa ktora mefunguje:
    #ingredients = models.One(Ingredients, on_delete = models.CASCADE , related_name = "Ingredients", blank = True, null = True)
    def __str__(self):
        return self.name



#ked menis strukturu databazy tak musis urobit makemigrations
