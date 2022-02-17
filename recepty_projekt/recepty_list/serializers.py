class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        field = ('name', 'grams')

class ReceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recept
        field = ('name', 'author', 'cooking time', 'portions', 'difficulty', 'ingredients')

