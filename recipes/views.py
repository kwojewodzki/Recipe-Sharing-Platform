from django.shortcuts import render
from rest_framework import views, permissions, generics
from rest_framework.response import Response

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
# Create your views here.

class RecipesView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer