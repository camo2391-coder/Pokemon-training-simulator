import pymysql
import pandas as pd
import config.database_config as db_config
import config.app_config as app_config

def connect_db():
    conn = pymysql.connect(
        host= db_config.DB_HOST,
        port = db_config.DB_PORT,
        user = db_config.DB_USER,
        password = db_config.DB_PASSWORD,
        database = db_config.DB_NAME
    )
    return conn

def print_pokemon():
    poke_id1 = input("Enter Pokemon ID or name: ")
    conn = connect_db()
    cursor = conn.cursor()
    query1 = app_config.QUERY1
    # Busca por ID o NOMBRE para cada Pokémon
    cursor.execute(query1, ('%' + poke_id1 + '%',))
    rows = cursor.fetchall()
    pokemon_data = pd.DataFrame(rows, columns = app_config.POKEMON_BASE_COLUMNS)
    cursor.close()
    conn.close()
    print(pokemon_data)
    return None

def grab_pokemons(poke_id1, poke_id2):
    conn = connect_db()
    cursor = conn.cursor()
    # Busca por ID o NOMBRE para cada Pokémon
    query2 = app_config.QUERY2
    cursor.execute(query2, (poke_id1, poke_id1, poke_id2, poke_id2, poke_id1, poke_id1, poke_id2, poke_id2))
    rows = cursor.fetchall()
    pokemon_data = pd.DataFrame(rows, columns = app_config.POKEMON_BASE_COLUMNS_WITH_TYPES)
    cursor.close()
    conn.close()
    return pokemon_data

def display_pokemons():
    poke_id1 = input("Enter first Pokemon ID or name: ").lower()
    poke_id2 = input("Enter second Pokemon ID or name: ").lower()
    pokemons = grab_pokemons(poke_id1, poke_id2)
    pokemons = generate_pokemon_EVs(pokemons)
    pokemons = generate_pokemon_level(pokemons)
    #print only first pokemon ATK_EV column
    #print(pokemons.loc[0, 'ATK_EV'])
    stats_calculation(pokemons)

def get_valid_EV(stat_name):
    while True:
        try:
            ev = int(input(f"Enter EV for {stat_name} (0-252): "))
            if 0 <= ev <= 252:
                return ev
            else:
                print("EV must be between 0 and 252.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_pokemon_EVs(pokemons):
    pokemons_evs = pd.DataFrame(index=pokemons.index, columns = app_config.POKEMON_EV_COLUMNS)
    for pokemon in pokemons.itertuples():
        print(f"Insert the EVs for Pokemon ({pokemon.POKE_NAME}):")
        HP_EV = get_valid_EV("HP")
        ATK_EV = get_valid_EV("ATK")
        DEF_EV = get_valid_EV("DEF")
        SPATK_EV = get_valid_EV("SPATK")
        SPDEF_EV = get_valid_EV("SPDEF")
        SPD_EV = get_valid_EV("SPD")
        if (HP_EV + ATK_EV + DEF_EV + SPATK_EV + SPDEF_EV + SPD_EV) > 510:
            print("Error: Total EVs cannot exceed 510, enter correct values.")
            return generate_pokemon_EVs(pokemons)
        else:
            pokemons_evs.loc[pokemon.Index] = [HP_EV, ATK_EV, DEF_EV, SPATK_EV, SPDEF_EV, SPD_EV] 
    return pd.concat([pokemons, pokemons_evs], axis=1)

def generate_pokemon_level(pokemons):
    pokemons_lvl = pd.DataFrame(index=pokemons.index, columns = app_config.POKEMON_LVL)
    for pokemon in pokemons.itertuples():
        print(f"Insert the level for Pokemon ({pokemon.POKE_NAME}):")
        try:
            poke_level = int(input("Enter level (1-100): "))
            if not (1 <= poke_level <= 100):
                print("Error: Level must be between 1 and 100, enter correct value.")
                return generate_pokemon_level(pokemons)
            else:
                pokemons_lvl.loc[pokemon.Index] = poke_level
        except ValueError:
            print("Please enter a valid integer.")
            return generate_pokemon_level(pokemons)
    return pd.concat([pokemons, pokemons_lvl], axis=1)

def stats_calculation(pokemons):
    poke_stats = pd.DataFrame(index=pokemons.index, columns = app_config.POKEMON_FINAL_STATS_COLUMNS)
    for poke in pokemons.itertuples():
        HP = round(0.01*(2*poke.HP + 31 + 0.25*poke.HP_EV)*poke.POKE_LVL + poke.POKE_LVL + 10)
        ATK = round(0.01*(2*poke.ATK + 31 + 0.25*poke.ATK_EV)*poke.POKE_LVL + 5)
        DEF = round(0.01*(2*poke.DEF + 31 + 0.25*poke.DEF_EV)*poke.POKE_LVL + 5)
        SPATK = round(0.01*(2*poke.SPATK + 31 + 0.25*poke.SPATK_EV)*poke.POKE_LVL + 5)
        SPDEF = round(0.01*(2*poke.SPDEF + 31 + 0.25*poke.SPDEF_EV)*poke.POKE_LVL + 5)
        SPD = round(0.01*(2*poke.SPD + 31 + 0.25*poke.SPD_EV)*poke.POKE_LVL + 5)
        poke_stats.loc[poke.Index] = [HP, ATK, DEF, SPATK, SPDEF, SPD]
    poke_stats = pd.concat([pokemons[app_config.POKEMON_NAME_LVL], poke_stats], axis=1)
    print(poke_stats)

def main():
    display_pokemons()

main()
