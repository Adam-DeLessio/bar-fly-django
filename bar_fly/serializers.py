from rest_framework import serializers
from recipes.models import Recipe

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
    	model = Ingredient
    	fields = ('id', 'name',)