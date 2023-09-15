from django.urls import path
from . import views

urlpatterns = [
    path('', views.allPokemon, name='all_pokemon'),
    path('pokemon/', views.getPokemon, name='get_pokemon'),
]
