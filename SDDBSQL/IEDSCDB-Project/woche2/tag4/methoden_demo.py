import math

class Punkt2D:
    anzahl_punkte = 0
    def __init__(self, x=0.0, y=0.0):   # Default is (0.0, 0.0) if no values are given.
        self.x = x
        self.y = y

    def abstand_nullpunkt(self):              #Calculates distance from (0, 0) using: sqroot(x2 + y2)	Example: (3,4) → distance = 5.
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def spiegeln(self, axis):     # reflect
        if axis == "x":
            self.y = -self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("Achse ungültig:", axis)

    # Reflects the point across an axis:
    # "x" → flip vertically(change sign of y)
    # "y" → flip horizontally(change sign of x)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        # return self.x == other.x and self.y == other.y # OR
        return (type(self) == type(other)
                and self.x == other.x
                and self.y == other.y)
    # Destruktor
    def __del__(self):
        Punkt2D.anzahl_punkte -= 1

    @classmethod
    def print_anzahl(cls):
        print(f"anzahl Punkte: {cls.anzahl_punkte}")

def main():
    p = Punkt2D(4.5, 7.2)
    print(p, "Abstand zu Nullpunkt:", p.abstand_nullpunkt())
    p.spiegeln("y")
    print(p)

    # Ü: Klassenvariable anzahl_punkte, klassenmethode print_anzahl,
    # eine Liste mit einigen Punkten erzeugen

    punkte = [Punkt2D(4.5, -5.7), Punkt2D(), Punkt2D(x=1.4)]
    for i in punkte:
        print(i)
    Punkt2D.print_anzahl()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# set_punkte = {Punkt2D(7, 2), Punkt2D(7, 2)}
# print("Inhalt von set_punkte: ")
# for p in set_punkte:
#     print(p, end=" ")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    q1 = Punkt2D(5, -6)
    q2 = Punkt2D(5, -6)
    print(q1, q2, "Gleich:", q1 == q2)
    print(q1 == "Sonne", q1 == q2)  #ruft automatisch __eq__auf

    r = Punkt2D()
    Punkt2D.print_anzahl()
    del r  # Objekt wird aus Speicher entfernt, hat keinen anderen Variablennamen
    Punkt2D.print_anzahl()


if __name__ == "__main__":
    main()
