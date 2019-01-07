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
        self._goalkeepers = []
        self._defenders = []
        self._midfielders = []
        self._forwards = []

    def __str__(self):
        string = "===%s===\n" % (self.name.upper())
        string += "===GOALKEEPERS===\n"
        for p in self._goalkeepers:
            string += str(p)
        string += "===DEFENDERS===\n"
        for p in self._defenders:
            string += str(p)
        string += "===MIDFIELDERS===\n"
        for p in self._midfielders:
            string += str(p)
        string += "===FORWARDS===\n"
        for p in self._forwards:
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
        self._goalkeepers.append(player)
        return "Added %s to goalkeepers" % player.name

    def add_defender(self, player):
        self._defenders.append(player)
        return "Added %s to defenders" % player.name

    def add_midfielder(self, player):
        self._midfielders.append(player)
        return "Added %s to midfielders" % player.name

    def add_forward(self, player):
        self._forwards.append(player)
        return "Added %s to forwards" % player.name

    def sort_by_score(self):
        self._goalkeepers.sort(key=lambda x: x.score, reverse=True)
        self._defenders.sort(key=lambda x: x.score, reverse=True)
        self._midfielders.sort(key=lambda x: x.score, reverse=True)
        self._forwards.sort(key=lambda x: x.score, reverse=True)

    def best_lineup(self):
        return Lineup.best_lineup(self)

    def goalkeepers(self):
        return self._goalkeepers

    def defenders(self):
        return self._defenders

    def midfielders(self):
        return self._midfielders

    def forwards(self):
        return self._forwards


class Lineup:

    def __init__(self, formation):
        self.players = []
        self.formation = formation

    @staticmethod
    def best_lineup(squad):
        possible_formations = [
            (3, 4, 3),
            (3, 5, 2),
            (4, 3, 3),
            (4, 4, 2),
            (4, 5, 1),
            (5, 3, 2),
            (5, 4, 1)
        ]
        possible_lineups = []
        if type(squad) is Squad:
            squad.sort_by_score()
            for formation in possible_formations:
                temp_lineup = Lineup(formation)
                try:
                    best_goalkeeper = squad.goalkeepers()[0]
                    temp_lineup.lineup_a_player(best_goalkeeper)
                except IndexError:
                    temp_lineup.lineup_a_player(Player("INVALID PLAYER", Position.GOALKEEPER, -4))
                for i in range(0, formation[0]):
                    try:
                        best_defender = squad.defenders()[i]
                        temp_lineup.lineup_a_player(best_defender)
                    except IndexError:
                        temp_lineup.lineup_a_player(Player("INVALID PLAYER", Position.DEFENDER, -4))
                for i in range(0, formation[1]):
                    try:
                        best_midfielder = squad.midfielders()[i]
                        temp_lineup.lineup_a_player(best_midfielder)
                    except IndexError:
                        temp_lineup.lineup_a_player(Player("INVALID PLAYER", Position.MIDFIELDER, -4))
                for i in range(0, formation[2]):
                    try:
                        best_forward = squad.forwards()[i]
                        temp_lineup.lineup_a_player(best_forward)
                    except IndexError:
                        temp_lineup.lineup_a_player(Player("INVALID PLAYER", Position.FORWARD, -4))
                possible_lineups.append(temp_lineup)
            possible_lineups.sort(key=lambda x: x.lineup_total_score(), reverse=True)
            return possible_lineups[0]
        else:
            return None

    def lineup_total_score(self):
        total_score = 0
        for player in self.players:
            total_score += player.score
        return total_score

    def lineup_a_player(self, player):
        self.players.append(player)

    def __str__(self):
        temp_squad = Squad("LINEUP %d %d %d" % (self.formation[0], self.formation[1], self.formation[2]))
        for player in self.players:
            temp_squad.add_player(player)
        return temp_squad.__str__()+"===TOTAL SCORE  %d===" % (self.lineup_total_score())


# Possible formation
# 3-4-3
# 3-5-2

# 4-3-3
# 4-4-2
# 4-5-1

# 5-3-2
# 5-4-1
