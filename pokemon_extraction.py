#program to call PokeApi and get details of a pokemon
import requests
import pandas as pd
import time

start = time.perf_counter()

def human_readable(seconds: float) -> str:
    ms = int((seconds - int(seconds)) * 1000)
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}h {m}m {s}s {ms}ms"
    if m:
        return f"{m}m {s}s {ms}ms"
    return f"{s}s {ms}ms"

BASE_URL_MAIN = "https://pokeapi.co/api/v2/pokemon/"
poke_range = range(1, 1026)  # First generation Pokémon IDs
df_poke_main = pd.DataFrame()
df_poke_abilities = pd.DataFrame()
df_pokemon_types = pd.DataFrame()

for poke_id in poke_range:
    try:
        response = requests.get(BASE_URL_MAIN + str(poke_id))
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon: {e}")
        exit()

    try:
        species_response = requests.get(data['species']['url'])
        species_data = species_response.json()
        poke_generation = species_data['generation']['name']
        poke_generation = poke_generation.replace('generation-', '')
    except:
        poke_generation = "Unknown"
    
    poke_name = data['name']
    poke_stats = pd.json_normalize(data["stats"])
    poke_stats = poke_stats.drop(columns=['effort', 'stat.url', 'stat.name'])
    poke_bst = sum(poke_stats['base_stat'])

    # Map abilities by 'slot' to ensure correct placement of ABILITY_1/2/3
    poke_ability_1 = None
    poke_ability_2 = None
    poke_ability_3 = None
    for abil in data.get('abilities', []):
        name = abil['ability']['name']
        slot = abil.get('slot')  # normalmente 1, 2 o 3
        if slot == 1:
            poke_ability_1 = name
        elif slot == 2:
            poke_ability_2 = name
        elif slot == 3:
            poke_ability_3 = name
        else:
            # fallback: si viene marcado como hidden o para completar el siguiente vacío
            if abil.get('is_hidden'):
                poke_ability_3 = name
            elif poke_ability_1 is None:
                poke_ability_1 = name
            elif poke_ability_2 is None:
                poke_ability_2 = name
            else:
                poke_ability_3 = poke_ability_3 or name

    pokemon_types = [t['type']['name'] for t in data['types']]

    pokemon_main_row = [poke_id, poke_name] + poke_stats['base_stat'].tolist() + [poke_bst, poke_generation]
    pokemon_df = pd.DataFrame([pokemon_main_row], columns=['POKE_ID', 'POKE_NAME', 'HP', 'ATK', 'DEF', 'SPATK', 'SPDEF', 'SPD', 'BST', 'GEN_INTRODUCTION'])
    
    pokemon_abilities_row = [poke_id, poke_ability_1, poke_ability_2, poke_ability_3]
    pokemon_abilities_df = pd.DataFrame([pokemon_abilities_row], columns=['POKE_ID', 'ABILITY_1', 'ABILITY_2', 'ABILITY_3'])

    pokemon_types_row = [poke_id] + pokemon_types + [None]*(2 - len(pokemon_types))  # Fill up to 2 types
    pokemon_types_df = pd.DataFrame([pokemon_types_row], columns=['POKE_ID', 'TYPE_1', 'TYPE_2'])

    df_poke_main = pd.concat([df_poke_main, pokemon_df], ignore_index=True)  # Agregar fila al DataFrame
    df_poke_abilities = pd.concat([df_poke_abilities, pokemon_abilities_df], ignore_index=True)
    df_pokemon_types = pd.concat([df_pokemon_types, pokemon_types_df], ignore_index=True)
    
#print(df_poke_main)
df_poke_main.to_csv('pokemon_main_1stgen.csv', index=False, header=False)
df_poke_abilities.to_csv('pokemon_abilities_1stgen.csv', index=False, header=False)
df_pokemon_types.to_csv('pokemon_types_1stgen.csv', index=False, header=False)

print("Data extraction complete. CSV files created.")

end = time.perf_counter()
elapsed = end - start
print("Execution time:", human_readable(elapsed))