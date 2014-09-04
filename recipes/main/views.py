from django.shortcuts import render
from django.http import HttpResponse
import re

from django.views.generic.base import View

from main.models import Recipe, Ingredient, Category, Direction

class Recipes(View):
    def get(self, request, recipe_id=None):
        if recipe_id is None:
            recipes = Recipe.objects.all()
            return render(request, 'recipes.html', {'recipes':recipes})
        else:
            recipe = Recipe.objects.get(id=recipe_id)
            ingredients = Ingredient.objects.filter(recipe__id=recipe_id)
            directions = Direction.objects.filter(recipe__id=recipe_id).order_by('step')
            return render(request, 'recipe.html', {'recipe':recipe,
                                                   'ingredients':ingredients,
                                                   'directions':directions})