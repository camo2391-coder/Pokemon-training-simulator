#program to call PokeApi and get details of a pokemon
import requests
import pandas as pd

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
usr_input = input("Enter the name of the Pokemon (in case the pokemon name has spaces, use hyphens e.g. mr-mime):")

try:
    response = requests.get(BASE_URL + usr_input.lower())
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching Pokémon: {e}")
    exit()

try:
    species_response = requests.get(data['species']['url'])
    species_data = species_response.json()
    generation = species_data['generation']['name']
except:
    generation = "Unknown"

df_stats = pd.json_normalize(data["stats"])
df_stats = df_stats.drop(columns=['effort', 'stat.url'])

df_abilities = pd.json_normalize(data["abilities"])
df_abilities = df_abilities.drop(columns=['ability.url','slot'])

types = [t['type']['name'] for t in data['types']]

print(f"Pokedex entry: {data['id']}")
print(f"Pokemon name: {data['name']}")
print(f"Types: {', '.join(types)}")
print(f"Base stat total: {sum(df_stats['base_stat'])}")
print(f"Pokemon stats:\n{df_stats}")
print(f"Pokemon abilities:\n{df_abilities}")
print(f"Introduced in generation: {generation}")



# ACCEDER A STAT PARTICULAR df.iloc[3,0] > OUTPUT = 145 (special-attack)