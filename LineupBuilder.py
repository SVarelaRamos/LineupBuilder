from SquadManager import *

my_players = [
    Player("Rubén Blanco", Position.GOALKEEPER, 2),
    Player("Santamaría", Position.GOALKEEPER, 10),
    Player("Alex Moreno", Position.DEFENDER, 6),
    Player("Álvaro González", Position.DEFENDER, -2),
    Player("Rubén Duarte", Position.DEFENDER, 2),
    Player("Akieme", Position.DEFENDER, 0),
    Player("Vallejo", Position.DEFENDER, 0),
    Player("Rochina", Position.MIDFIELDER, 10),
    Player("Muniain", Position.MIDFIELDER, -2),
    Player("Trigueros", Position.MIDFIELDER, 6),
    Player("Wakaso", Position.MIDFIELDER, 2),
    Player("Raba", Position.MIDFIELDER, 0),
    Player("Aduriz", Position.FORWARD, 2),
    Player("Verde", Position.FORWARD, 6),
    Player("Santi Mina", Position.FORWARD, 16)
]
my_squad = Squad("CarreiroTeam")
for player in my_players:
    my_squad.add_player(player)

print(my_squad)

my_squad.sort_by_score()

print(my_squad)

print(my_squad.best_lineup())

#Posible lineups
# 3-4-3
# 3-5-2

# 4-3-3
# 4-4-2
# 4-5-1

# 5-3-2
# 5-4-1