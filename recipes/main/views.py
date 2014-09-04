from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View

from main.models import Recipe, Ingredient, Category

# Create your views here.

class RecipeCollectionView(View):

    def get(self, request, sort="alphabetical", pivot=None):
        ''' The method is responsible for handling collection get requests'''
        
        resource_dict = {}

        template = 'index.html'
        
        if sort == 'ingredient':
            if pivot:
                pivot = Ingredient.objects.get(pk=pivot)
                bucket = pivot.recipe_set.all()
            else:
                bucket = Ingredient.objects.all()
            
        elif sort == 'category':
            if pivot:
                pivot = Category.objects.get(pk=pivot)
                bucket = pivot.recipe_set.all()
            else:
                bucket = Category.objects.all()
        else:
            bucket = Recipe.objects.all()

        for drop in bucket:
            
            key = drop.name.upper()[0]

            if key not in resource_dict:
                resource_dict[key] = list()

            resource_dict[key].append(drop)

        return render(request, template, {'resource_collection': resource_dict, 'title': sort, 'pivot': pivot } )

    def post(self, request):
        '''Handles posts of new recipes from a form'''

        return HttpResponse('POST /')

class RecipeResourceView(View):
    def get(self, request, pivot=None):
        return HttpResponse('Would return a single recipe object with id %s' % (pivot))
