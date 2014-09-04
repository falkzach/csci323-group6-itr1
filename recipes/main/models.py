from django.db import models


class Ingredient(models.Model):

    name = models.CharField(max_length=255,)
    unit_of_measure = models.CharField(max_length=255,null=True,blank=True)
    value_of_measure = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class Direction(models.Model):

    step = models.IntegerField(unique=True)
    description = models.CharField(max_length=2048,null=True,blank=True)

    def __str__(self):
        return str(self.step)

class Recipe(models.Model):

    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,null=True,blank=True)
    rating = models.IntegerField(null=True,blank=True)

    ingredients = models.ManyToManyField(Ingredient,null=True,blank=True)

    directions = models.ManyToManyField(Direction,null=True,blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=255,)
    description = models.CharField(max_length=255,null=True,blank=True)

    recipes = models.ManyToManyField(Recipe,null=True,blank=True)

    def __str__(self):
        return self.name
