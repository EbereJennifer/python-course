import random
from aufgabe5_1 import Produkt


pool_namen = ["smartphone", "notebook", "Tablet", "PC", "Monitor", "Drucker"]
pool_preise = [499, 600, 299.95, 598.80]
pool_begleittexte = ["Grandios", "Bahnbrechend", "Hervorrangend", "Cringe"]


liste = [
    Produkt(
        random.randint(500_000, 800_000),
        random. choice(pool_namen),
        random.choice(pool_preise),
        random.choice(pool_begleittexte)
    ) for _ in range(10)
]

def sort_produkte(produkt_liste, key):
    produkt_liste.sort(key=key)

def printout(liste):
    for elem in liste:
        print ("#" * 40)


sort_produkte(liste, lambda elem: elem.name)
printout(liste)

sort_produkte(liste, lambda elem: elem.preis)
printout(liste)

def get_id(produkt):
    return produkt.produkt_id

sort_produkte(liste, key=get_id)
printout(liste)


