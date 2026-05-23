
class Ergebnisliste:
    def __init__(self, tag, zahlen):
        self.tag = tag
        self.zahlen = zahlen

    def __str__(self):
        return f"Ergebnisliste Tag: {self.tag} {self.zahlen}"

    def __repr__(self):
        return f"Ergebnisliste(tag={self.tag!r}, zahlen={self.zahlen!r})"   # !r means: use repr() instead of str()
                                                                            # Ergebnisliste(tag='Monday', zahlen=[1, 2, 3])
    def __eq__(self, other):
        return (
            type(self) == type(other)
            and self.tag == other.tag
            and self.zahlen == other.zahlen
        )

    # Kein Prüfungsstoff
    # Nötig: Detailliert auf immutable eingehen
    # Nötig, um Element in set zu sein, oder um key in dict zu sein
    # Required: Discuss immutability in detail
    # Required for an element to be in a set or for a key to be in a dictionary
    def __hash__(self):
        return hash((self.tag, tuple(self.zahlen)))   # Lists are mutable (changeable) → NOT allowed in hashing
                                                        # Tuples are immutable → safe for hashing
                                                        # so this code means reate a unique numeric ID based on tag and zahlen, so this object can be used in sets or dictionary keys.”
    def __add__(self, other):
        assert isinstance(other, Ergebnisliste)        # Ensures other is the same class, If not → program crashes with an error

        if self.tag != other.tag:                              # Only allow addition if both objects have the same tag, Otherwise → error
            raise ValueError("Ergebnislisten can only be added if tag is the same")

        return Ergebnisliste(self.tag, self.zahlen + other.zahlen)  # self.zahlen + other.zahlen -> This concatenates the lists
                                                                                # (not adding numbers!)
    def __lt__(self, other):
        if not isinstance(other, Ergebnisliste):
            return NotImplemented
        if self.tag == other.tag:
            return sum(self.zahlen) < sum(other.zahlen)
        else:
            return self.tag < other.tag


erg_liste_1 = Ergebnisliste("04-21", [5, 8, 4, 3])
print(erg_liste_1)

erg_liste_2 = Ergebnisliste("04-21", [5, 8, 4, 3])
print(erg_liste_1 == erg_liste_2)

set = {erg_liste_1, erg_liste_2}
print(set)
print("*" * 50)

erg_liste_3 = Ergebnisliste("04-21", [9, 5, 3, 8])
erg_liste_4 = erg_liste_1 + erg_liste_3
print(erg_liste_4)

erg_liste_5a = Ergebnisliste("04-24", [4, 9, 6])
erg_liste_5b = Ergebnisliste("04-24", [5, 3, 1, 2])

erg_liste_6 = Ergebnisliste("03-20", [1, 6, 1, 4])
erg_liste_7 = Ergebnisliste("04-18", [5])

print("*" * 40)

gesamt_liste = [erg_liste_1, erg_liste_5b, erg_liste_6, erg_liste_7, erg_liste_5a]
for elem in gesamt_liste:
    print(elem)
print("*" * 40)
for elem in sorted(gesamt_liste):
    print(elem)

print(repr(erg_liste_5a))

