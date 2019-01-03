from enum import Enum


class Position(Enum):
    GOALKEEPER = 1
    DEFENDER = 2
    MIDFIELDER = 3
    FORWARD = 4


class Player:

    def __init__(self, name, position, score):
        self.name = name
        self.position = position
        self.score = score

    def __str__(self):
        return "%-20s %3d\n" % (self.name, self.score)


class Squad:

    def __init__(self, name):
        self.name = name
        self.goalkeepers = []
        self.defenders = []
        self.midfielders = []
        self.forwards = []

    def __str__(self):
        string = "===%s===\n" % (self.name.upper())
        string += "===GOALKEEPERS===\n"
        for p in self.goalkeepers:
            string += str(p)
        string += "===DEFENDERS===\n"
        for p in self.defenders:
            string += str(p)
        string += "===MIDFIELDERS===\n"
        for p in self.midfielders:
            string += str(p)
        string += "===FORWARDS===\n"
        for p in self.forwards:
            string += str(p)

        return string

    def add_player(self, player):
        if type(player) == Player:
            # todo: map this?
            if player.position == Position.GOALKEEPER:
                self.add_goalkeeper(player)
            elif player.position == Position.DEFENDER:
                self.add_defender(player)
            elif player.position == Position.MIDFIELDER:
                self.add_midfielder(player)
            elif player.position == Position.FORWARD:
                self.add_forward(player)
        else:
            print("NOT A PLAYER")

    def add_goalkeeper(self, player):
        self.goalkeepers.append(player)
        return "Added %s to goalkeepers" % player.name

    def add_defender(self, player):
        self.defenders.append(player)
        return "Added %s to defenders" % player.name

    def add_midfielder(self, player):
        self.midfielders.append(player)
        return "Added %s to midfielders" % player.name

    def add_forward(self, player):
        self.forwards.append(player)
        return "Added %s to forwards" % player.name

    def sort_by_score(self):
        self.goalkeepers.sort(key=lambda x: x.score, reverse=True)
        self.defenders.sort(key=lambda x: x.score, reverse=True)
        self.midfielders.sort(key=lambda x: x.score, reverse=True)
        self.forwards.sort(key=lambda x: x.score, reverse=True)
