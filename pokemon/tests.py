from django.test import TestCase, Client
from .views import POKEAPI_BASE_URL
from django.urls import reverse

class PokemonViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_allPokemon_success(self):
        url = reverse('all_pokemon')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('pokemons', data)

    def test_getPokemon_success(self):
        url = reverse('get_pokemon')
        response = self.client.get(url, {'name': 'bulbasaur'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('bulbasaur', data)

    def test_getPokemon_not_found(self):
        url = reverse('get_pokemon')
        response = self.client.get(url, {'name': 'nonexistentpokemon'})
        self.assertEqual(response.status_code, 404)

    def test_getPokemon_no_name(self):
        url = reverse('get_pokemon')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
