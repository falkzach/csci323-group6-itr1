from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View

from main.models import Recipe, Ingredient, Category

class Recipes(View):
    def get(self, request, id=None):
        recipes = Recipe.objects.all()
        return render(request, 'recipes.html', {'recipes':recipes})
