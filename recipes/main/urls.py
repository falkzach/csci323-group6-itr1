from django.conf.urls import url

from main.views import Recipes, Categories

urlpatterns = [
        url(r'^$', Recipes.as_view()),
        url(r'^recipes$', Recipes.as_view(), name="recipes"),
        url(r'^recipes/(?P<recipe_id>[0-9]+)$', Recipes.as_view(), name="recipe"),
        url(r'^categories$', Categories.as_view(), name="categories"),
        url(r'^categories/(?P<category_id>[0-9]+)$', Categories.as_view(), name="category"),

]