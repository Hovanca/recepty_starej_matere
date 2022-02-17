from django.contrib import admin
from .models import Recept
from .models import Ingredients
# Register your models here.

class ReceptyAdmin(admin.ModelAdmin):
    list_display = ('name','author')

admin.site.register(Recept, ReceptyAdmin)
#neviem ci chcem ingredience vypisovat yet