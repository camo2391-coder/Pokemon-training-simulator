#program to call PokeApi and get details of a pokemon
import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
#usr_input = input("Enter the name of the Pokemon (in case the pokemon name has spaces, use hyphens e.g. mr-mime):")

poke_list = range(1,11) #list of first 10 pokemon IDs

for i in poke_list:
    try:
        response = requests.get(BASE_URL + str(i))
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon: {e}")
        exit()

    with open(data['name'] + ".json", "w", encoding="utf-8") as archivo:
        json.dump(response.json(), archivo, indent=2)
    print(f"Downloaded data for Pokémon ID: {i}, name: {data['name']}")