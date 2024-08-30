from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon:Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return "Caught {} with health {}".format(pokemon.name, pokemon.health)
        else:
            return "This pokemon is already caught"
    
    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon_name == pokemon.name:
                self.pokemons.remove(pokemon)
                return "You have released {}".format(pokemon_name)
            else:
                 return "Pokemon is not caught"
    
    def trainer_data(self):
        details = []
        details.append("Pokemon trainer: {}".format(self.name))
        details.append("Pokemon count: {}".format(len(self.pokemons)))
        for pokemon in self.pokemons:
            details.append("- {}".format(pokemon.pokemon_details()))
            
        return "\n".join(details)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())