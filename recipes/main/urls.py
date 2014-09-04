from django.conf.urls import url

from main.views import Recipes

urlpatterns = [
        url(r'^$', Recipes.as_view()),

]