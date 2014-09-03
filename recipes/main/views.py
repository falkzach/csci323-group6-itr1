from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View

from main.models import Recipe, Ingredient

# Create your views here.

class RecipeCollectionView(View):

    def get(self, request, sort=None, pivot=None):
        ''' The method is responsible for handling collection get requests'''
        
        recipe_dict = {}
        
        if sort == 'ingredient':
            # Use the ingredeint
            bucket = Ingredient.objects.all()
        else:
            # If not sort is specified just get all recipes
            bucket = Recipe.objects.all()

        for drop in bucket:
            
            key = drop.name.upper()[0]

            if key not in recipe_dict:
                recipe_dict[key] = list()

            recipe_dict[key].append(drop)

        return render(request, 'index.html', {'recipes': recipe_dict})

    def post(self, request):
        '''Handles posts of new recipes from a form'''

        return HttpResponse('POST /')

class RecipeResourceView(View):
    def get(self, request, id=None):
        return HttpResponse('Would return a single recipe object with id %s' % (id))
