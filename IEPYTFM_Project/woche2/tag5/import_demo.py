import random     # Alle inhalte des Moduls stehen bereit, lange Name einsch. Modulename

random.choice([1, 2, 3])     #Modulnamen, Funktionsname
random.random()              # Modulnamen, Funktionsname




# choice([4, 5, 6,])   # nur Funktionsname, nicht erlaubt
# random()   # der Compiler denkt, dass der Modul aufgerufen werden soll


# import mit from: Einzelne Sachen können mit dem kurzen Namen verwendet werden
from random import choices, randint

choices([2, 4, 5, 6], k=3)
randint(1, 6)

