"""
2)
Skript player.py
Klasse Player mit 4 Instanzattributen (name, birthday, score, is_active).
Methoden für Stringdarstellung und Vergleich auf inhaltliche Gleichheit.
Klassenmethode read() liest 4 Werte von Konsole und erzeugt daraus ein Player-Objekt.

2)
Script player.py
Player class with 4 instance attributes (name, birthday, score, is_active).
Methods for string representation and comparison of content.
The class method read() reads 4 values from the console and uses them to create a Player object.

"""
class Player:
    def __init__(self, name, birthday, score, is_active):
        self.name = name
        self.birthday = birthday
        self.score = score
        self.is_active = is_active

    def __str__(self):
        return f"Name: {self.name}, Birthday: {self.birthday}, Score: {self.score}, Active: {self.is_active}"

    def __eq__(self, other):
        if isinstance(other, Player):
            return (self.name == other.name and
                    self.birthday == other.birthday and
                    self.score == other.score and
                    self.is_active == other.is_active)
        return False

    @classmethod
    def read(cls):
        name = input("Enter name: ")
        birthday = input("Enter birthday (YYYY-MM-DD): ")
        score = float(input("Enter score: "))
        is_active_input = input("Is active (True/False): ")

        # convert string to boolean
        is_active = is_active_input.lower() == "true"

        return cls(name, birthday, score, is_active)    # # cls(...) creates a new Player instance

p1 = Player.read()
p2 = Player.read()

print(p1)
print(p2)

print("Equal?", p1 == p2)

# This is a test code. Python executes files top to bottom.
# It first reads and defines the class
# Then it reaches your test code
# Then it runs it
# If you put the test code before the class → Player doesn’t exist yet → error
if __name__ == "__main__":
    p1 = Player.read()
    print(p1)

