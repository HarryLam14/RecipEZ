from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from pages.serializers import RecipeSerializer
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


# def index(request):
#     query = ["granulated sugar",
#             "shortening",
#             "eggs",
#             "flour",
#             "cream of tartar",
#             "baking soda",
#             "vanilla extract"]
#     recipes = Recipe.objects.filter(ingredients__name__in=query).annotate(recipe_count=Count('name')).order_by('-recipe_count').values('name', 'rating')[:50]
    # counts = collections.Counter(recipes)
    # ordered = sorted(recipes, key=lambda x: (counts[x], x), reverse=True)
    # results = list(dict.fromkeys(ordered))
# 
    # return HttpResponse('\n'.join(str(recipes)))

@api_view(['GET'])
def search(request):
    query = [request.query_params.getlist('ingredients')]
    recipes = Recipe.objects.filter(ingredients__name__in=query).annotate(recipe_count=Count('name')).order_by('-recipe_count').values('name', 'rating')[:50]

    return HttpResponse((recipes))

@api_view(['POST'])
def search(request):
    # recipe = Recipe.objects.filter(ingredients__name__in=request.data)
    # if request.method == 'GET':
        
    #     counts = collections.Counter(recipe)
    #     ordered = sorted(recipe, key=lambda x: (counts[x], x), reverse=True)
    #     results = list(dict.fromkeys(ordered))

    #     return JsonResponse(results)

    if request.method == 'POST':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        if recipe_serializer.is_valid():
            return JsonResponse(recipe_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
