#Aufgabe 1:
#Vergleichsoperatoren <, <=, ==, !=, >, >= auf ganzen Zahlen ausprobieren.
#Rechenoperationen für Addition, Subtraktion und Multiplikation auf ganzen Zahlen ausprobieren.
#Multiplikationstafel ausgeben, mind. 3 mal 3
#1 2 3
#2 4 6
#3 6 9

a = 1
b = 2
c = 3


z = c > a
print("ist großer", z)

g = (b >= c)
print("nicht möglich", g)

g = (b == c)
print("es ist nicht gleich", g)

g = (b != c)
print("es ist nicht gleich", g)

g = c>a
print(g)
print(b <= a)
print(b > a)

print(2 + 4 + 6)
print(6-4)
print(2-4-6)
print(2*4-4)
print(4-2 /6)
#print(int(4-2 / 6))



#Aufgabe 2:
#Recherchieren: Exponentialschreibweise für Kommazahlen. Einige Werte so als Variable definieren (mind. 3 physikalische Konstanten nachschauen
# z.B.Avogadro-Konstante, Lichtgeschwindigkeit, ...)
#Ausrechnen: 100.00 € Startwert, jeweils 3% Zinsen kommen nach jedem Jahr dazu, Gesamtwert nach 1, 2, 3, ..., 10 Jahren

#Exponentialschreibweise Scientific notation is a way of expressing numbers that are too large or too small to be conveniently written in decimal form,
# since to do so would require writing out an inconveniently long string of digits. It may be referred to as scientific form or standard index form,
# or standard form in the United Kingdom.
#The Avogadro constant is 6.02214076 × 10²³ particles per mole, defining the number of atoms or molecules in one mole of a substance.


#e.g 300 = 3 * 10e2

Berlin_bevölkerung = 3.4 * 10e6
print(Berlin_bevölkerung)

x = 4.567 * 10e-2
print(x)

Avogadro_constant = 6.02214076 * 10e23
print("avogadro_constant:", Avogadro_constant)

speed_of_light = 3.0e8
print(speed_of_light)

lichtgeschwindigkeit = 186e3
print("lichtgeschwindigkeit:", lichtgeschwindigkeit)

gravitational_constant = 6.674e-11
print("gravitational constant:", gravitational_constant)


# Calculate: Starting value of €100.00; 3% interest added each year; total value after 1, 2, 3, ..., 10 years
# This is compound interest, meaning it grows like this:

# value = startwert × (1 + zinsen)^n
#n = Jahr

Startwert = 100
zinsen = 0.03


wert1 = 100 * (1 + zinsen)**1
print("wert nach 1 jahr:", wert1)


for Jahr in range(1, 11):
    Wert = Startwert * (1 + zinsen) ** Jahr
    print(f"Year {Jahr}: €{Wert:.2f}")


#correction
print(3 < 4, 8 <= 7, 8 == 8, 8 != 8, 6785 > 8272, 567 >= 0)

print("Ergebnis von 6 > 5:", 6 > 5)

a = 4
b = 3
summe = a + b
differenz = a - b
produkt = a * b

print("summe von", a, "und", b, ":", summe)
print("differenz von", a, "und", b, ":", differenz)
print("produkt von", a, "und", b, ":", produkt)


#1 2 3
#2 4 6
#3 6 9

# #Aufgabe 1:
# input-Funktion in Skript Aufgabe1.py ausprobieren. Werte für vier Variable der Typen String, ganza Zahl, Kommazahl,
# Wahrheitswert einlesen, Typen geeignet umwandeln.
# Alle Variable ausgeben, auch ihren Typ anzeigen.

name = input("name:")
print(type(name))

ganza_Zahl = (input("ganza_Zahl:"))
i = int(ganza_Zahl)
print("Eingabe war:", ganza_Zahl, "Ganza_Zahl:", i)

#kommazahl = float(input("float:")) the float function cannot convert a string to float. therefore input only integers or float. intergers will be converted to a float

kommazahl = float(input("float:"))
print("float value:", kommazahl, "kommazahl:")


kommazahl = input("float:")
f = float(kommazahl)
print("Eingabe war:", kommazahl, "kommazahl:", f)

Wahrheitswert = input("give bool:")
#Wahrheitswert = bool(Wahrheitswert) bool function cannot convert a string to bool.
b = bool(Wahrheitswert)
print("Eingabe war:", Wahrheitswert, "Wahrheitswert:", b)

if Wahrheitswert == "True":
    print("Wahrheitswert ist True")
elif Wahrheitswert == "False":
    print("Wahrheitswert ist False")
else:
    print("kein Wahrheitswert ist erkannt")



# Aufgabe 2:
# Als Skript den Namen einer Operation einlesen lassen, erlaubt Werte sollen sein: "Addition", "Multiplikation", "Potenz".
# Dann die entsprechende Operation mit den Variablen zahl1 und zahl2 ausführen, und das Ergebnis ansprechend ausgeben, z.B. "Die Addition von 12 und 13 liefert 25."
# Write a script that prompts the user to enter the name of an operation; the allowed values are: “Addition,” “Multiplication,” and “Exponentiation.”
# Then perform the corresponding operation using the variables num1 and num2, and display the result in a clear and concise manner,
# e.g., “The sum of 12 and 13 is 25.”
# fallunterscheidung, if-statement


num1 = 12
num2 = 13
ergebnis = 0

name_einer_operation = input("erlaubt werte sind (addition, multiplikation, Potenz):")

if name_einer_operation == "addition":
    ergebnis = num1 + num2
    print(f"Die Addition von {12} und {13} liefert {ergebnis} ")
    #print("Die Addition von", num1, "und" num2, "liefert", ergebnis, ".")  this is another method to print
elif name_einer_operation == "multiplikation":
    ergebnis = num1 * num2
    print(f"Die multiplikation von {12} und {13} liefert {ergebnis} ")
    #print("Die multiplikation von", num1, "und", num2 "liefert", ergebnis, ".")
elif name_einer_operation == "exponentiation":
    ergebnis = num1 ** num2
    print(f"Die Potenz {12} und {13} liefert {ergebnis} ")
else:
    print("Das war eine falsche Zahl.")

#correction
#Aufgabe 1:
input1 = input("Eingabe String: ")
print("Eingabe war:", input1)

input2 = input("Eingabe ganze Zahl: ")
n = int(input2)
print("Eingabe war:", input2, "Ganza_Zahl:", n)

input3 = input("Eingabe Kommazahl: ")
f = float(input3)
print("Eingabe war:", input3, "Kommazahl:", f)

input4 = input("Eingabe wahrheitswert: ")
b = bool(input4)






