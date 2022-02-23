from django.db import models
from rest_framework import viewsets

#IMAGE HANDLING
from io import BytesIO  #basic input/output operation
from PIL import Image #Imported to compress images
from django.core.files import File #to store files

def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


class Photos(models.Model):
    image = models.ImageField(upload_to='uploads/')

    # calling image compression function before saving the data
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.image


# Create your models here.

class Ingredients(viewsets.ModelViewSet):
    name = models.CharField(max_length = 50)
    grams = models.IntegerField()

    def __str__(self):
        return self.name

class Recept(viewsets.ModelViewSet):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    #thumbnail = Photos() davame zatial na bok
    cooking_time = models.DurationField() #treba mi njast argumenty na minuty
    #https://www.geeksforgeeks.org/durationfield-django-models/ toto niekde musis pridat
    #https://pytutorial.com/django-durationField-examples
    portions = models.IntegerField()
    #difficulty = DifficultyForm()
    #mozno to je zle https://www.geeksforgeeks.org/choicefield-django-forms/
    #ingredients = Ingredients()


    def __str__(self):
        return self.name



