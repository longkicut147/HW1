class SteamUser:
    def __init__(self, username, games:list):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return "{} is playing {}".format(self.username, game)
        else:
            return "{} is not in library".format(game)
        
    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return "{} bought {}".format(self.username, game)
        else:
            return "{} is already in your library".format(game)
        
    def status(self):
        games_count = len(self.games)
        return "{} has {} games. Total play time: {}".format(self.username, games_count, self.played_hours)
    
user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
