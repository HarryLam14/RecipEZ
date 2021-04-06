from django.db import models


# Create your models here.
class Recipe(models.Model):
    recipe_id = models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length = 200)
    steps = models.CharField(max_length = 200)

class Ingredient(models.Model):
    ingredient_id = models.IntegerField(primary_key=True)
    ingredient_name = models.CharField(max_length = 200)
    recipes = models.ManyToManyField(Recipe)

# class UserIngredients(models.Model):


# class Join(models.Model):
#     recipe_id = models.ForeignKey()
#     ingredient_id = models.ForeignKey()