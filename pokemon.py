import ast
import numpy as np
global attack_multiplier_matrix
global POKEMON_TYPES
global POKEMON_NATURE

POKEMON_TYPES = {
    0: "Normal",
    1: "Fire",
    2: "Water",
    3: "Grass",
    4: "Electric",
    5: "Ground",
    6: "Fighting",
    7: "Flying",
    8: "Rock",
    9: "Bug",
    10: "Psychic",
    11: "Dark",
    12: "Ghost",
    13: "Poison",
    14: "Ice",
    15: "Steel",
    16: "Dragon",
    17: "Fairy",
}

POKEMON_NATURE = {
    1:  {"name": "Adamant",     "modifiers": (1, 1.1, 1, 0.9, 1, 1)},
    2:  {"name": "Modest",      "modifiers": (1, 0.9, 1, 1.1, 1, 1)},
    3:  {"name": "Jolly",       "modifiers": (1, 1, 1, 0.9, 1, 1.1)},
    4:  {"name": "Bold",        "modifiers": (1, 0.9, 1.1, 1, 1, 1)},
    5:  {"name": "Calm",        "modifiers": (1, 0.9, 1, 1, 1.1, 1)},
    6:  {"name": "Timid",       "modifiers": (1, 0.9, 1, 1, 1, 1.1)},
    7:  {"name": "Impish",      "modifiers": (1, 1, 1.1, 0.9, 1, 1)},
    8:  {"name": "Careful",     "modifiers": (1, 1, 1, 0.9, 1.1, 1)},
    9:  {"name": "Naughty",     "modifiers": (1, 1.1, 1, 1, 0.9, 1)},
    10: {"name": "Quiet",       "modifiers": (1, 1, 1, 1.1, 1, 0.9)},
    11: {"name": "Brave",       "modifiers": (1, 1.1, 1, 1, 1, 0.9)},
    12: {"name": "Relaxed",     "modifiers": (1, 1, 1.1, 1, 1, 0.9)},
    13: {"name": "Sassy",       "modifiers": (1, 1, 1, 1, 1.1, 0.9)},
    14: {"name": "Lonely",      "modifiers": (1, 1.1, 0.9, 1, 1, 1)},
    15: {"name": "Rash",        "modifiers": (1, 1, 1, 1.1, 0.9, 1)},
    16: {"name": "Lax",         "modifiers": (1, 1, 1.1, 1, 0.9, 1)},
    17: {"name": "Mild",        "modifiers": (1, 1, 0.9, 1.1, 1, 1)},
    18: {"name": "Gentle",      "modifiers": (1, 1, 0.9, 1, 1.1, 1)},
    19: {"name": "Hasty",       "modifiers": (1, 1, 0.9, 1, 1, 1.1)},
    20: {"name": "Naive",       "modifiers": (1, 1, 1, 1, 0.9, 1.1)},
    21: {"name": "Bashful",     "modifiers": (1, 1, 1, 1, 1, 1)},
    22: {"name": "Docile",      "modifiers": (1, 1, 1, 1, 1, 1)},
    23: {"name": "Hardy",       "modifiers": (1, 1, 1, 1, 1, 1)},
    24: {"name": "Quirky",      "modifiers": (1, 1, 1, 1, 1, 1)},
    25: {"name": "Serious",     "modifiers": (1, 1, 1, 1, 1, 1)}
}

attack_multiplier_matrix = [
    [1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,0.5,1.0,1.0,1.0,0.0,1.0,1.0,0.5,1.0,1.0],
    [1.0,0.5,0.5,2.0,1.0,1.0,1.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0,2.0,2.0,0.5,1.0],
    [1.0,2.0,0.5,0.5,1.0,2.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0],
    [1.0,0.5,2.0,0.5,1.0,2.0,1.0,0.5,2.0,0.5,1.0,1.0,1.0,0.5,1.0,0.5,0.5,1.0],
    [1.0,1.0,2.0,0.5,0.5,0.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0],
    [1.0,2.0,1.0,0.5,2.0,1.0,1.0,0.0,2.0,0.5,1.0,1.0,1.0,2.0,1.0,2.0,1.0,1.0],
    [2.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,2.0,0.5,0.5,2.0,0.0,0.5,2.0,2.0,1.0,0.5],
    [1.0,1.0,1.0,2.0,0.5,1.0,2.0,1.0,0.5,2.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0],
    [1.0,2.0,1.0,1.0,1.0,0.5,0.5,2.0,1.0,2.0,1.0,1.0,1.0,1.0,2.0,0.5,1.0,1.0],
    [1.0,0.5,1.0,2.0,1.0,1.0,0.5,0.5,1.0,1.0,2.0,2.0,0.5,0.5,1.0,0.5,1.0,0.5],
    [1.0,1.0,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,0.5,0.0,1.0,2.0,1.0,0.5,1.0,1.0],
    [1.0,1.0,1.0,1.0,1.0,1.0,0.5,1.0,1.0,1.0,2.0,0.5,2.0,1.0,1.0,1.0,1.0,0.5],
    [0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,2.0,0.5,2.0,1.0,1.0,1.0,1.0,1.0],
    [1.0,1.0,1.0,2.0,1.0,0.5,1.0,1.0,0.5,1.0,1.0,1.0,0.5,0.5,1.0,0.0,1.0,2.0],
    [1.0,0.5,0.5,2.0,1.0,2.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,0.5,2.0,1.0],
    [1.0,0.5,0.5,1.0,0.5,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,1.0,2.0,0.5,1.0,2.0],
    [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.5,2.0,0.0],
    [1.0,0.5,1.0,1.0,1.0,1.0,2.0,1.0,1.0,1.0,1.0,2.0,1.0,0.5,1.0,0.5,2.0,1.0]
]

class pokemon:
    def __init__(self, name, typing, base_stats, poke_level, poke_IVs, poke_EVs, nature):
        self.name = name
        self.typing = typing
        self.base_stats = base_stats
        self.poke_level = poke_level
        self.poke_IVs = poke_IVs
        self.poke_EVs = poke_EVs
        self.nature = nature
 
    def printID(self):
        if len(self.typing) == 1:
            return f"My name is {self.name} and my type is {POKEMON_TYPES[self.typing[0]]}!"
        elif len(self.typing) == 2:
            return f"My name is {self.name} and my types are {POKEMON_TYPES[self.typing[0]]} and {POKEMON_TYPES[self.typing[1]]}!"
        else:
            return f"Error in typing definition"
        
    def printSTATS(self):
        return f"My name is {self.name} and these are my base stats:\n\tHP: {self.base_stats[0]}\n\tATK: {self.base_stats[1]}\n\tDEF: {self.base_stats[2]}\n\tSPATK: {self.base_stats[3]}\n\tSPDEF: {self.base_stats[4]}\n\tSPD: {self.base_stats[5]}\n\t"
    
    def printLVL(self):
        return f"My level is {self.poke_level}"
    
    def printNATURE(self):
        return f"My nature is: {POKEMON_NATURE[self.nature]['name']} and my modifiers are:{POKEMON_NATURE[self.nature]['modifiers']}"


    def printFINAL_STATS(self):
        poke_HP = round(0.01*(2*self.base_stats[0] + self.poke_IVs[0] + 0.25*self.poke_EVs[0])*self.poke_level + self.poke_level + 10)
        poke_ATK = round(0.01*(2*self.base_stats[1] + self.poke_IVs[1] + 0.25*self.poke_EVs[1])*self.poke_level + 5)
        poke_DEF = round(0.01*(2*self.base_stats[2] + self.poke_IVs[2] + 0.25*self.poke_EVs[2])*self.poke_level + 5)
        poke_SPATK = round(0.01*(2*self.base_stats[3] + self.poke_IVs[3] + 0.25*self.poke_EVs[3])*self.poke_level + 5)
        poke_SPDEF = round(0.01*(2*self.base_stats[4] + self.poke_IVs[4] + 0.25*self.poke_EVs[4])*self.poke_level + 5)
        poke_SPE = round(0.01*(2*self.base_stats[5] + self.poke_IVs[5] + 0.25*self.poke_EVs[5])*self.poke_level + 5)

        poke_stats_no_nature = np.array([poke_HP,poke_ATK,poke_DEF,poke_SPATK,poke_SPDEF,poke_SPE])
        nature_modifiers = np.array(POKEMON_NATURE[self.nature]["modifiers"])
        poke_stats_not_rounded = poke_stats_no_nature*nature_modifiers
        poke_stats = tuple(round(x) for x in poke_stats_not_rounded)
        return f"\tHP: {poke_stats[0]}\n\tATK: {poke_stats[1]}\n\tDEF: {poke_stats[2]}\n\tSPATK: {poke_stats[3]}\n\tSPDEF: {poke_stats[4]}\n\tSPD: {poke_stats[5]}"

def attack_multiplier(attack_type, poke):
    multiplier = 1
    for poke_type in poke.typing:
        multiplier *= attack_multiplier_matrix[attack_type][poke_type]
    return multiplier

def battle(pokemon1, pokemon2):
    return f"This is the first battle ever between {pokemon1.name} and {pokemon2.name}. Who will win?!"

def validate_EVs(poke_EVs):
    if all(individual_EV <= 252 for individual_EV in poke_EVs) and sum(poke_EVs) <= 510:
        return 1
    else:
        return 0

def create_pokemon():
    #ast.literal_eval se usa para interpretar el input(tipo string) como estructura de python (int, tuple, float, etc)
    poke_name = input("Pokemon's name': ")
    poke_typing = ast.literal_eval(input("Pokemon's type: "))
    poke_base_stats = ast.literal_eval(input("Pokemon's base stats: "))
    poke_level = ast.literal_eval(input("Pokemon's level:"))
    poke_IVs = ast.literal_eval(input("Pokemon IVs: "))
    poke_EVs = ast.literal_eval(input("Pokemon EVs: "))
    print("Pokemon nature (Choose a number from the list):")
    for nature_id, nature in POKEMON_NATURE.items():
        print(f"{nature_id} - {nature['name']}")
    poke_nature = ast.literal_eval(input())
    if validate_EVs(poke_EVs):
        poke = pokemon(poke_name, poke_typing, poke_base_stats, poke_level, poke_IVs, poke_EVs, poke_nature)
        return poke
    else:
        print("Insert propper EVs: maximun individual EV is 252 and combined EVs maximun 510")
        

def main():

    user_pokemon = create_pokemon()
    print(user_pokemon.printID())
    print(user_pokemon.printSTATS())
    print(user_pokemon.printLVL())
    print(user_pokemon.printNATURE())
    print(user_pokemon.printFINAL_STATS())

main()