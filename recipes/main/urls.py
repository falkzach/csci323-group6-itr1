from django.conf.urls import url

from main.views import RecipeCollectionView

urlpatterns = [
        url(r'^$', RecipeCollectionView.as_view()),
]
