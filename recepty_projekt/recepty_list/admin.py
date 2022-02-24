from django.contrib import admin
from .models import Recept, Ingredient


class ReceptyAdmin(admin.ModelAdmin):
    list_display = ('name','cooking_time','author')

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name','grams')

admin.site.register(Recept, ReceptyAdmin)
admin.site.register(Ingredient, IngredientsAdmin)
#neviem ci chcem ingredience vypisovat yet