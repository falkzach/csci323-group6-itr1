from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import View

# Create your views here.

class RecipeCollectionView(View):
    http_method_names = ['get', 'post']

    def get(self, request):
        ''' The method is responsible for handling collection get requests'''

        return HttpResponse('GET /')

    def post(self, request):
        '''Handles posts of new recipes from a form'''

        return HttpResponse('POST /')
