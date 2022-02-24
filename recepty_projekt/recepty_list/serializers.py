from rest_framework import serializers
from .models import Ingredient, Recept
#tu vytvarame jsony


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'grams')

class ReceptSerializer(serializers.ModelSerializer):
    difficulty = serializers.StringRelatedField(many = False)
    ingredients = IngredientsSerializer(many = True, read_only = True)
    class Meta:
        model = Recept
        fields = ('name', 'author','thumbnail', 'cooking_time', 'portions','difficulty','ingredients')

