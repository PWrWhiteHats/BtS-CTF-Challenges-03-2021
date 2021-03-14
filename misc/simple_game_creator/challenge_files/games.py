from conf import flag 

class Multiplayer(object):
    def __init__(self, name, difficulty, players):
        self.name = name
        self.difficulty = "easy" # No one will create hard game, no need to implement it
        self.players = players

    def show_details(self):
        print('{0.players} can play this easy game called ' + self.name).format(self)

class Singleplayer(object):
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = "easy" 

    def show_details(self):
        print("This " + self.difficulty + " game is called " + self.name)

class CTFGame(object):
    def __init__(self):
        self.flag = flag