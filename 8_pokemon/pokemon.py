class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return "{} with health {}".format(self.name, self.health)