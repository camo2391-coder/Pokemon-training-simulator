import ast
global attack_multiplier_matrix

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
    def __init__(self, name, typing, base_stats, poke_level, poke_EVs):
        self.name = name
        self.typing = typing
        self.base_stats = base_stats
        self.poke_level = poke_level
        self.poke_EVs = poke_EVs
 
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
    poke_EVs = ast.literal_eval(input("Pokemon EVs: "))
    if validate_EVs(poke_EVs):
        poke = pokemon(poke_name, poke_typing, poke_base_stats, poke_level, poke_EVs)
        return poke
    else:
        print("Insert propper EVs: maximun individual EV is 252 and combined EVs maximun 510")

def main():

    user_pokemon = create_pokemon()
    print(user_pokemon.printID())
    print(user_pokemon.printSTATS())
    print(user_pokemon.printLVL())

main()