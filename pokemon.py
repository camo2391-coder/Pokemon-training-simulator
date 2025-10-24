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
    def __init__(self, name, typing):
        self.name = name
        self.typing = typing
 
    def printID(self):
        if len(self.typing) == 1:
            return f"My name is {self.name} and my type is {POKEMON_TYPES[self.typing[0]]}!"
        elif len(self.typing) == 2:
            return f"My name is {self.name} and my types are {POKEMON_TYPES[self.typing[0]]} and {POKEMON_TYPES[self.typing[1]]}!"
        else:
            return f"Error in typing definition"

def attack_multiplier(attack_type, poke):
    multiplier = 1
    for poke_type in poke.typing:
        multiplier *= attack_multiplier_matrix[attack_type][poke_type]
    return multiplier


def battle(pokemon1, pokemon2):
    return f"This is the first battle ever between {pokemon1.name} and {pokemon2.name}. Who will win?!"

def main():

    pikachu = pokemon('Pikachu',(4,))
    onyx = pokemon('Onix',(8,))
    gengar = pokemon('Gengar',(12,13))
    parasect = pokemon('Parasect',(3,9))
    dragonite = pokemon('Dragonite',(16,))
    reshiram = pokemon('Reshiram',(16,1))

    print(pikachu.printID())
    print(onyx.printID())
    print(gengar.printID())

    print(battle(pikachu,onyx))
    print(attack_multiplier(2,reshiram))

main()
