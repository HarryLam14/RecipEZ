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
from django.core.paginator import Paginator
import collections

# Create your views here.
from .models import Recipe, Ingredient

def index(request):
    return render(request, 'index.html')

def recipes_list(request):
    recipes = Recipe.objects.all()
    disp_items =  10 # request.GET.get('items') could be useful instead
    paginator = Paginator(recipes, disp_items)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'recipes.html', {'page_obj': page_obj})

@api_view(['GET'])
def search(request):
    query = [request.query_params.getlist('ingredients')]
    recipes = Recipe.objects.filter(ingredients__name__in=query).annotate(recipe_count=Count('name')).order_by('-recipe_count').values('name', 'rating')[:50]

    return HttpResponse((recipes))
