from django.urls import path
from . import views

urlpatterns = [
    path('', views.allPokemon, name='allPokemon'),
    path('pokemon/', views.getPokemon, name='getPokemon'),
]
