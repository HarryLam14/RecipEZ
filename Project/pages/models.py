from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length=255)
    minutes = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.JSONField()
    nutrition = models.JSONField(blank=True, null=True)
    rating = models.IntegerField()
    n_ratings = models.IntegerField()

    def __str__(self):
        return self.name
