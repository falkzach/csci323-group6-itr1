from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View

# Create your views here.

class RecipeCollectionView(View):

    def get(self, request, sort=None, pivot=None):
        ''' The method is responsible for handling collection get requests'''

        if sort == 'alphabetical':
            if pivot:
                return HttpResponse('Would return list of recipes using letter %s' % (pivot))
            else:
                return HttpResponse('Would return list of all recipes ordered by letter')

        elif sort == 'ingredient':
            if pivot:
                return HttpResponse('Would return list of recipes using ingredient %s' % (pivot))
            else:
                return HttpResponse('Would return list of all recipes ordered by ingredient ')
        elif sort == 'category':
            if pivot:
                return HttpResponse('Would return list of recipes using category %s' % (pivot))
            else:
                return HttpResponse('Would return list of recipes in ordered by category')
        else:
            return HttpResponse('Would return list of recipes in chronological order')

    def post(self, request):
        '''Handles posts of new recipes from a form'''

        return HttpResponse('POST /')

class RecipeResourceView(View):
    def get(self, request, id=None):
        return HttpResponse('Would return a single recipe object with id %s' % (id))
