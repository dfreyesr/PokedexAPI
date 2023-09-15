import requests
from django.http import JsonResponse

POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2/pokemon?offset=0&limit=1281'

def fetch_data_from_url(url):
    """Fetch data from the given URL. Return the JSON content or None if request fails."""
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None


def allPokemon(request):
    """Return a list of all Pokemon from the POKEAPI or a 500 error if fetching fails."""
    data = fetch_data_from_url(POKEAPI_BASE_URL)
    if data:
        pokemons = data.get('results', [])
        return JsonResponse({'pokemons': pokemons})
    return JsonResponse({'error': 'Failed to fetch pokemon data'}, status=500)


def getPokemon(request):
    """Retrieve details of a specific Pokemon by name. Return a 404 error if Pokemon is not found."""
    pokemon_name = request.GET.get('name')
    data = fetch_data_from_url(POKEAPI_BASE_URL)

    if data:
        pokemons = data.get('results', [])
        detail_url = next((pokemon["url"] for pokemon in pokemons if pokemon["name"] == pokemon_name), None)

        if detail_url:
            abilities_data = {"abilities": getAbilities(detail_url)}
            details = getDetails(detail_url)
            return JsonResponse({pokemon_name: [abilities_data] + details})
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

    return JsonResponse({'error': 'Failed to fetch pokemon data'}, status=500)


def getDetails(detailUrl):
    """Return the type, Pokedex ID, and sprite details of a Pokemon from the given URL."""
    data = fetch_data_from_url(detailUrl)

    if data:
        return [
            {"type": data.get('types', [])[0]["type"]["name"]},
            {"pokedexId": data.get('id')},
            {"sprites": data.get('sprites')}
        ]
    return []


def getAbilities(detailUrl):
    """Retrieve and return the abilities of a Pokemon from the given URL."""
    data = fetch_data_from_url(detailUrl)

    if data:
        abilities = data.get('abilities', [])
        return [{"name": ability["ability"]["name"], "detail": getAbilitiesDetail(ability["ability"]["url"])} for ability in abilities]
    return []


def getAbilitiesDetail(abilityUrl):
    """Fetch and return the English description of a Pokemon's ability from the given URL."""
    data = fetch_data_from_url(abilityUrl)

    if data:
        details = data.get('effect_entries', [])
        return next((detail["effect"] for detail in details if detail["language"]["name"] == "en"), None)
    return None
