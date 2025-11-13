#program to call PokeApi and get details of a pokemon
import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
usr_input = input("Enter the name of the Pokemon (in case the pokemon name has spaces, use hyphens e.g. mr-mime):")

try:
    response = requests.get(BASE_URL + usr_input.lower())
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching Pokémon: {e}")
    exit()

with open(usr_input.lower() + ".json", "w", encoding="utf-8") as archivo:
    json.dump(response.json(), archivo, indent=2)
