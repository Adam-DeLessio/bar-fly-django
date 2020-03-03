
from django.shortcuts import render, redirect
from rest_framework import generics
# from .models import Recipe
# from .serializers import RecipeSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Ingredient
from .serializers import IngredientSerializer
from django.core.management.base import BaseCommand
import requests



@api_view(['GET', 'POST'])
def IngredientList(request):
	if request.method == 'GET':
		data = Ingredient.objects.all()
		serializer = IngredientSerializer(data, context={'request': request}, many=True)
		return Response(serializer.data)





# @api_view(['GET', 'POST'])
# def RecipeList(request):
#     if request.method == 'GET':
#         data = Recipe.objects.all()
#         serializer = RecipeSerializer(data, context={'request': request}, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = RecipeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'DELETE'])
# def RecipeDetail(request, pk):
#     if request.method == 'GET':
#         recipe = Recipe.objects.get(pk=pk)
#         serializer = RecipeSerializer(recipe, context={'request': request})
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         recipe = Recipe.objects.get(pk=pk).delete()