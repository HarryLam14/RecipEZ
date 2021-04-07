from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import collections

# Create your views here.
from .models import Recipe, Ingredient

def index(request):
    return render(request, 'index.html')

def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes.html', context)


def index(request):
    recipe = Recipe.objects.filter(ingredients__name__in=['cooked sweet potato','tart cooking apple', 'cola', 'kiwi fruits', 'salt'])
    counts = collections.Counter(recipe)
    ordered = sorted(recipe, key=lambda x: (counts[x], x), reverse=True)
    results = list(dict.fromkeys(ordered))

    return HttpResponse('\n'.join(str(results)))

