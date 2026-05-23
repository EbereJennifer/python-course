"""
Klasse Player mit 4 Instanzattributen (name, birthday, score, is_active).
Methoden für Stringdarstellung und Vergleich auf inhaltliche Gleichheit.
Klassenmethode read() liest 4 Werte von Konsole und erzeugt daraus ein Player-Objekt.
"""

from datetime import date

class Player:
    format_de = "%d.%m.%Y"
    def __init__(self, name, birthday, score, is_active):
        self.name = name
        self.birthday = birthday
        self.score = score
        self.is_active = is_active

    def __str__(self):
        return f"Player {self.name}, Geburtstag: {self.birthday.strftime(Player.format_de)}, Score: {self.score}, Aktiv: {self.is_active}"

    @classmethod
    def read(cls):
        name, birthday, score, is_active = input("Eingabe name, birthday, score, is_active (y/n): ").split(", ")
        birthday = date.strptime(birthday, Player.format_de)
        score = int(score)
        is_active = (is_active == "y")
        return Player(name, birthday, score, is_active)


def main():
    Player.read()


if __name__ == "__main__":
    main()



