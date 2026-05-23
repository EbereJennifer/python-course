"""
#Fehlerbehandlung, damit Programm nicht bei Error abstürzt
# else und finally können fehlen
"""

#Error handling to prevent the program from crashing when an error occurs
# The `else` and `finally` blocks may be omitted
try:
    n = 5 // 1
    print("Nach Division durch 0")
except ZeroDivisionError:
    print("Das war eine Division durch 0") # nur im Fehlerfall
else: # this means no error is happening
    print(f"Hat geklappt. Ergebnis: {n}")
finally:
    print("In finally")

try:
    zahl_als_string = input("Eingabe Zahl:")
    zahl = int(zahl_als_string)
except ValueError: #input a wrong value e.g juhvifnfj but "123" would give you "ende"
    print("Das war keine korrekte Eingabe")
print("Ende")