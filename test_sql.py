import pymysql
import pandas as pd

df = pd.DataFrame()

conn = pymysql.connect(
    host='localhost',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'pokemon_ddbb'
)

def grab_pokemon(poke_id1, poke_id2):
    cursor = conn.cursor()
    # Busca por ID o NOMBRE para cada Pokémon
    query = """
    SELECT POKE_NAME, ATK, SPD FROM pokemon_main 
    WHERE (POKE_ID = %s OR POKE_NAME = %s) 
       OR (POKE_ID = %s OR POKE_NAME = %s)
    """
    cursor.execute(query, (poke_id1, poke_id1, poke_id2, poke_id2))
    rows = cursor.fetchall()
    pokemon_data = pd.DataFrame(rows, columns=['POKE_NAME', 'ATK', 'SPD'])
    cursor.close()
    conn.close()
    return pokemon_data

def main():
    poke_id1 = input("Enter first Pokemon ID or name: ")
    poke_id2 = input("Enter second Pokemon ID or name: ")
    pokemons = grab_pokemon(poke_id1, poke_id2)
    print(pokemons)

main()
