from django.contrib import admin
from recipes.main.models import Recipe, Ingredient, Category


admin.autodiscover()

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Category)
