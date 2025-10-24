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

class pokemon:
    def __init__(self, name, typing, stats):
        self.name = name
        self.typing = typing
        self.stats = stats
 
    def printID(self):
        if len(self.typing) == 1:
            return f"My name is {self.name} and my type is {POKEMON_TYPES[self.typing[0]]}!"
        elif len(self.typing) == 2:
            return f"My name is {self.name} and my types are {POKEMON_TYPES[self.typing[0]]} and {POKEMON_TYPES[self.typing[1]]}!"
        else:
            return f"Error in typing definition"
        
    def printSTATS(self):
        return f"My stats are:\n\tHP: {self.stats[0]}\n\tATK: {self.stats[1]}\n\tDEF: {self.stats[2]}\n\t \
            SPATK: {self.stats[3]}\n\tSPDEF: {self.stats[4]}\n\tSPD: {self.stats[5]}\n\t"



def battle(pokemon1, pokemon2):
    return f"This is the first battle ever between {pokemon1.name} and {pokemon2.name}. Who will win?!"

def main():
    pikachu = pokemon('Pikachu',(4,),(35,55,40,50,50,90))
    onyx = pokemon('Onix',(8,),(35,45,160,30,45,70))
    gengar = pokemon('Gengar',(12,13),(60,65,60,130,75,110))

    print(pikachu.printID())
    print(onyx.printID())
    print(gengar.printID())

    print(battle(pikachu,onyx))
    print(gengar.printSTATS())

main()
