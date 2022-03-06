from django.db import models
from io import BytesIO
from PIL import Image
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile

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

    thumbnail = models.ImageField(upload_to = "recepty/")
    #dame si tu funkciu save ktora overrunne saving process
    def save(self, *args, **kwargs):
        self.thumbnail = self.compress(self.thumbnail)
        super(Recept,self).save(*args, **kwargs)

    def compress(self, uploaded_image):
        im = Image.open(uploaded_image)
        im_io = BytesIO()
        im_res = im.resize((1020, 573))
        im.save(im_io, format = 'JPEG', quality=60)
        #new_image = File(im_io, name=image.name)
        im_io.seek(0)
        new_image = InMemoryUploadedFile(im_io, 'ImageField', "%s.jpg" % uploaded_image.name.split('.')[0],
                                             'image/jpeg', sys.getsizeof(im_io), None)
        return new_image


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
