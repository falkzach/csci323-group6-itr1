from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound


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
            categories = Category.objects.all().filter(recipes__id=recipe_id)
            return render(request, 'recipe.html', {'recipe' : recipe,
                                                   'ingredients' : ingredients,
                                                   'directions' : directions,
                                                   'categories' : categories})

class Categories(View):
    def get(self, request, category_id=None):
        if category_id is None:
            categories = Category.objects.all()
            return render(request, 'categories.html', {'categories':categories})
        else:
            category = Category.objects.get(id=category_id)
            recipes = Recipe.objects.all().filter(category__id=category_id)
            return render(request, 'category.html', {'category':category,
                                                     'recipes':recipes})
