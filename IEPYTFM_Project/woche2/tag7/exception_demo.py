# Ü: 100 mal Division mit zufallszahlen im Bereich 0 - 10 durchführen,
# Ergebnisse aufsummieren. Bei division durch 0 Exception abfangen und mit 0 als
#Ergebnis weiterrechen
# Perform division 100 times with random numbers in the range 0 - 10,
# Sum up the results. Catch an exception when dividing by 0 and continue calculating with 0 as
# the result

import random
sum = 0
for _ in range(100):
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)

    try:
        ergebnis = n1 / n2
    except ZeroDivisionError:
        ergebnis = 0
        sum += ergebnis


print("Sum of all answers: ", sum)


# From Anton

summe = 0

for _ in range(100):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    try:
        c = a / b
        summe += c
    except ZeroDivisionError as e:
        print(e)


print(summe)

print()
# Nur als Beispiel
try:
    input("***** Testeingabe 1. Versuch: ")
except KeyboardInterrupt:
    input("********** Testeingabe 2. Versuch: ")

print("Programm geht weiter")