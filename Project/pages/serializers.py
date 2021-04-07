from rest_framework import serializers 
from pages.models import Recipe

 
class RecipeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Recipe
        fields = ('id',
                  'name',
                  'description',
                  'minutes',
                  'ingredients',
                  'steps',
                  'nutrition',
                  'rating',
                  'n_ratings')