from django.db import models


class Ingredient(models.Model):

    name = models.CharField(max_length=255,)
    unit_of_measure = models.CharField(max_length=255,)
    value_of_measure = models.CharField(max_length=255,)

    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)

    def __str__(self):
        return self.name

class Recipe(models.Model):

    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)
    rating = models.IntegerField()

    ingredients = models.ManyToManyField(Ingredient)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name



class Direction(models.Model):

    step = models.IntegerField()
    description = models.CharField(max_length=2048)

    recipe = models.ForeignKey(Recipe)

    def __str__(self):
        return self.step
