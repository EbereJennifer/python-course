"""
Schleife fragt ab, ob noch ein weiterer Durchgang erfolgen soll und
lässt pro Durchgang einen Player einlesen.
Nach der Schleife sollen alle Player-Objekte in einer Liste sein und
numeriert ausgegeben werden.

The loop checks whether another iteration should be performed and
reads in one player per iteration.
After the loop, all player objects should be in a list and
displayed in numerical order.
"""

from player import Player

liste = []

while True:
    eingabe = input("Soll eine Runde folgen? y/n: ")
    if eingabe == "y":
        player = Player. read()
        print("player eingelesen")
        liste.append(player)
    else:
        print("Ende ereicht")
        break

for i, player in enumerate(liste, start=1):
    print(f"{i}) {player}")