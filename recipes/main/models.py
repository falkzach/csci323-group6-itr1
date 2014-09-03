from django.db import models


class Recipe(models.Model):

    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)
    rating = models.IntegerField()

    # #further investigate relationships
    # ingredients = models.ManyToManyField(Ingredient)
    # categories = models.ManyToManyField(Category)
    # directions = models.ManyToManyField(Direction)

    def __str__(self):
        return self.name

class Ingredient(models.Model):

    name = models.CharField(max_length=255,)
    unit_of_measure = models.CharField(max_length=255,)
    value_of_measure = models.CharField(max_length=255,)

class Category(models.Model):

    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,)

class Direction(models.Model):

    step = models.IntegerField()
    description = models.CharField(max_length=2048)