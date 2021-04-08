from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('recipes', views.recipes_list, name = 'recipes'),
    url(r'^search', views.search),
    path('recipe', views.find_one, name= 'recipe'),
]
