# PokedexAPI

API middleware to access all pokemon's dsta and each pokemon's abilities, types, id and sprites.

# How to consume the API

To use this API:

`GET /`
Lists all the pokemons and the URL with its details.

`GET /pokemon/?name=pokemon`
Gets specificic pokemon's abilities, types, id and sprites. Uses param name which is the name of the pokemen we'll get.

For example
`/pokemon/?name=bulbasaur`

# To run this project

1. You need to set a virtual environment by executing the next commands:

`Python 3 -m venv myenv` <br>
`source myenv/bin/activate`

2. Then you need to install the dependencies by executing the next command:

`pip install -r requirements.txt`

3. Finally, to run this server you need to execude the next command:

`python manage.py runserver`

And now your server will be running on http://127.0.0.1:8000/
