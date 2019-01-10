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

    def __eq__(self, obj):
        return isinstance(obj, Player) and obj.name == self.name


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
        return Lineup.find_best_lineup(self)

    def goalkeepers(self):
        return self._goalkeepers

    def defenders(self):
        return self._defenders

    def midfielders(self):
        return self._midfielders

    def forwards(self):
        return self._forwards


class Lineup(Squad):

    def __init__(self, formation):
        lineup_name = "LINEUP %d %d %d" % (formation[0], formation[1], formation[2])
        Squad.__init__(self, lineup_name)
        self._formation = formation

    @staticmethod
    def find_best_lineup(squad):
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
            # Sorting by score we ensure that the low indexes are the best players
            squad.sort_by_score()

            # One possible lineup is no lineup in other words 11 "INVALID PLAYERS we will use 3-4-3 formation"
            temp_lineup = Lineup((3, 4, 3))
            temp_lineup.add_player(Player("INVALID PLAYER", Position.GOALKEEPER, -4))
            for i in range(0, 3):
                temp_lineup.add_player(Player("INVALID PLAYER", Position.DEFENDER, -4))
                temp_lineup.add_player(Player("INVALID PLAYER", Position.MIDFIELDER, -4))
                temp_lineup.add_player(Player("INVALID PLAYER", Position.FORWARD, -4))
            # Last midfielder missing is added here:
            temp_lineup.add_player(Player("INVALID PLAYER", Position.MIDFIELDER, -4))
            possible_lineups.append(temp_lineup)
            # Normal iteration between all possibilities
            for formation in possible_formations:
                temp_lineup = Lineup(formation)
                try:
                    best_goalkeeper = squad.goalkeepers()[0]
                    temp_lineup.add_player(best_goalkeeper)
                except IndexError:
                    temp_lineup.add_player(Player("INVALID PLAYER", Position.GOALKEEPER, -4))
                for i in range(0, formation[0]):
                    try:
                        best_defender = squad.defenders()[i]
                        temp_lineup.add_player(best_defender)
                    except IndexError:
                        temp_lineup.add_player(Player("INVALID PLAYER", Position.DEFENDER, -4))
                for i in range(0, formation[1]):
                    try:
                        best_midfielder = squad.midfielders()[i]
                        temp_lineup.add_player(best_midfielder)
                    except IndexError:
                        temp_lineup.add_player(Player("INVALID PLAYER", Position.MIDFIELDER, -4))
                for i in range(0, formation[2]):
                    try:
                        best_forward = squad.forwards()[i]
                        temp_lineup.add_player(best_forward)
                    except IndexError:
                        temp_lineup.add_player(Player("INVALID PLAYER", Position.FORWARD, -4))
                possible_lineups.append(temp_lineup)
            # Sorting lineups and returning the highest score
            possible_lineups.sort(key=lambda x: x.lineup_total_score(), reverse=True)
            return possible_lineups[0]
        else:
            return None

    def lineup_total_score(self):
        total_score = 0
        for p in self.goalkeepers():
            total_score += p.score
        for p in self.defenders():
            total_score += p.score
        for p in self.midfielders():
            total_score += p.score
        for p in self.forwards():
            total_score += p.score
        # If we don't lineup we get 0 points instead -44
        invalid_player_counter = self.goalkeepers().count(Player("INVALID PLAYER", Position.GOALKEEPER, -4)) + \
                                 self.defenders().count(Player("INVALID PLAYER", Position.DEFENDER, -4)) + \
                                 self.midfielders().count(Player("INVALID PLAYER", Position.MIDFIELDER, -4)) + \
                                 self.forwards().count(Player("INVALID PLAYER", Position.FORWARD, -4))
        return total_score if invalid_player_counter < 11 else 0

    def __str__(self):
        return super().__str__() + "===TOTAL SCORE  %d===" % (self.lineup_total_score())


# Possible formation
# 3-4-3
# 3-5-2

# 4-3-3
# 4-4-2
# 4-5-1

# 5-3-2
# 5-4-1
