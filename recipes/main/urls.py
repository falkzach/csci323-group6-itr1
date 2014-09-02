from django.conf.urls import url

from main.views import RecipeCollectionView, RecipeResourceView

urlpatterns = [
        url(r'^$', RecipeCollectionView.as_view()),
        url(r'^(?P<id>[0-9]+)$', RecipeResourceView.as_view()),
        url(r'^(?P<sort>alphabetical)$', RecipeCollectionView.as_view()),
        url(r'^(?P<sort>alphabetical)/(?P<pivot>[a-zA-Z])$', RecipeCollectionView.as_view()),
        url(r'^(?P<sort>ingredient|category)$', RecipeCollectionView.as_view()),
        url(r'^(?P<sort>ingredient|category)/(?P<pivot>[0-9]+)$', RecipeCollectionView.as_view()),
]
