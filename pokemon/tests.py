from django.test import TestCase, Client
from .views import POKEAPI_BASE_URL
from django.urls import reverse

class PokemonViewsTestCase(TestCase):

    def setUp(self):
        """Initialize test client for each test case."""
        self.client = Client()

    def test_allPokemon_success(self):
        """Ensure 'all_pokemon' view returns a 200 status code and contains 'pokemons' in its response."""
        url = reverse('all_pokemon')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('pokemons', data)

    def test_getPokemon_success(self):
        """Ensure 'get_pokemon' view returns data for 'bulbasaur' with a 200 status code."""
        url = reverse('get_pokemon')
        response = self.client.get(url, {'name': 'bulbasaur'})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('bulbasaur', data)

    def test_getPokemon_not_found(self):
        """Ensure 'get_pokemon' view returns a 404 status code for a nonexistent Pokemon."""
        url = reverse('get_pokemon')
        response = self.client.get(url, {'name': 'nonexistentpokemon'})
        self.assertEqual(response.status_code, 404)

    def test_getPokemon_no_name(self):
        """Ensure 'get_pokemon' view returns a 404 status code if no Pokemon name is provided."""
        url = reverse('get_pokemon')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)