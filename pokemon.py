class pokemon:
    def __init__(self, name, typing):
        self.name = name
        self.typing = typing
 
    def printID(self):
        if len(self.typing) == 1:
            return f"My name is {self.name} and my type is {self.typing[0]}!"
        elif len(self.typing) == 2:
            return f"My name is {self.name} and my types are {self.typing[0]} and {self.typing[1]}!"
        else:
            return f"Error in typing definition"

def battle(pokemon1, pokemon2):
    return f"This is the first battle ever between {pokemon1.name} and {pokemon2.name}. Who will win?!"


def main():
    pikachu = pokemon('Pikachu',('Electric',))
    onyx = pokemon('Onix',('Rock',))
    gengar = pokemon('Gengar',('Ghost','Poison'))

    print(pikachu.printID())
    print(onyx.printID())
    print(gengar.printID())

    print(battle(pikachu,onyx))

main()
