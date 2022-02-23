from rest_framework import serializers
from .models import Ingredients
from .models import Recept
#tu vytvarame jsony


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        field = ('name', 'grams')

class ReceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recept
        fields = ('name', 'author', 'cooking_time', 'portions')

