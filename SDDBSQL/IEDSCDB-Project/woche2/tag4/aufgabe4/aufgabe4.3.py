"""
In player_main.py
Schleife fragt ab, ob noch ein weiterer Durchgang erfolgen soll und lässt pro Durchgang einen Player einlesen.
Nach der Schleife sollen alle Player-Objekte in einer Liste sein und numeriert ausgegeben werden.

In player_main.py
A loop checks whether another iteration should be performed and loads one player per iteration.
After the loop, all player objects should be in a list and printed with their respective numbers.
"""

from player import Player

players = []

while True:
    p = Player.read()
    players.append(p)

    answer = input("Add another player? (y/n): ").lower()
    if answer != "y":
        break

print("\nAll players:")

for i, player in enumerate(players, start=1):
    print(f"{i}. {player}")

# What this teaches
# Using a loop with user control
# Storing objects in a list
# Using enumerate() to number output
# Separating logic into:
# player.py → class
# player_main.py → program flow

# From Anton

#< b > Anton
#Kölbl < / b >
from datetime import date


class Player:
    def __init__(self, name, birthday, score, is_active):
        self.name = name
        self.birthday = birthday
        self.score = score
        self.is_active = is_active

    def __str__(self):
        return f"Player {self.name}, Geburtstag: {self.birthday}, Score: {self.score}, Aktiv: {self.is_active}"

    @classmethod
    def read(cls):
        name, birthday, score, is_active = input("Eingabe name, birthday, score, is_active: ").split(", ")


Player.read()
