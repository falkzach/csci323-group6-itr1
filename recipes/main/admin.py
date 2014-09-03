from django.contrib import admin
from main.models import Recipe, Ingredient, Category, Direction


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Direction)

