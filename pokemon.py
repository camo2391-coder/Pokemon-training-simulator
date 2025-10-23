class pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def printID(self):
        return f"My name is {self.name} and my type is {self.type}"
    
def battle(pokemon1, pokemon2):
    return f"This is the first battle ever between {pokemon1.name} and {pokemon2.name}. Who will win?!"


def main():
    pikachu = pokemon('Pikachu','Electric')
    onyx = pokemon('Onix','Rock')

    print(pikachu.printID())
    print(onyx.printID())

    print(battle(pikachu,onyx))

main()
