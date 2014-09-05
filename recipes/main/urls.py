from django.conf.urls import url

from main.views import Recipes, Categories, Ingredients

urlpatterns = [
        url(r'^$', Recipes.as_view()),
        url(r'^recipes$', Recipes.as_view(), name="recipes"),
        url(r'^recipes/(?P<recipe_id>[0-9]+)$', Recipes.as_view(), name="recipe"),
        url(r'^categories$', Categories.as_view(), name="categories"),
        url(r'^categories/(?P<category_id>[0-9]+)$', Categories.as_view(), name="category"),
        url(r'^ingredients$', Ingredients.as_view(), name="ingredients"),
        url(r'^ingredients/(?P<ingredient_id>[0-9]+)$', Ingredients.as_view(), name="ingredient"),


]