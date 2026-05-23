from methoden_demo import Punkt2D

punkte = [
    Punkt2D(123, -45),
    Punkt2D(-343.56),
    Punkt2D(89.7, 73.5)
]
for i, p in enumerate(punkte, start=1):
    print(f"{i}. {p}")

liste = [p.x + p.y for p in punkte]
print(liste)   # comes this list from zahl not punkt