from flask import Flask, render_template
from .model import PokeClient
app = Flask(__name__)
app.jinja_env.filters['zip'] = zip
poke_client = PokeClient()

@app.route('/')
def index():
    """
    Must show all of the pokemon names as clickable links

    Check the README for more detail.
    """
    pokemon_ids = poke_client.get_pokemon_ids()
    pokemon_names = poke_client.get_pokemon_list()
    pokemon_data = zip(pokemon_names, pokemon_ids)
    
    return render_template('index.html', pokemon_data = pokemon_data)

@app.route('/pokemon/<pokemon_name>')
def pokemon_info(pokemon_name):
    """
    Must show all the info for a pokemon identified by name

    Check the README for more detail
    """
    pokemon_info = poke_client.get_pokemon_info(pokemon_name)
    
    return render_template('info.html', pokemon = pokemon_info)

@app.route('/ability/<ability_name>')
def pokemon_with_ability(ability_name):
    """
    Must show a list of pokemon 

    Check the README for more detail
    """
    pokemon_list = poke_client.get_pokemon_with_ability(ability_name)
    
    return render_template('ability.html', pokemon_list = pokemon_list, ability_name = ability_name)
