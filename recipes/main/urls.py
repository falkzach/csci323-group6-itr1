from django.conf.urls import url

from main.views import Recipes

urlpatterns = [
        url(r'^$', Recipes.as_view()),
        url(r'^recipes$', Recipes.as_view()),
        url(r'^recipes/(?P<recipe_id>[0-9]+)$', Recipes.as_view()),

]