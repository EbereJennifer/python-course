from selectors import SelectSelector

#hash symbol shows comments. wichtige Datentyben: Zeichenketten (Strings) entweder mit " oder ' erzeugen
s1 = "Hallo, Welt"
print(s1)

s2 = 'Guten Tag'
#ü: String s2 auf konsole anzeigen
print(s2)

#Ausgabe auf konsole, geht nicht zur nächsten Zeile weiter
print(s1, end="")
print(s2)

#Zwei wichtige Zahlentzýpen: int für ganze Zahlen, Float für kommazahlen
i = 16789 #i ist der Name für eine Variable
print(i)
i= 17687
print(i)

_= 345
print(_)

#Einige Variable mit Kommazahlen erzeugen und ausgeben. Diese Variablen werden als Gleitkommazahlen (Floats)
#Ü: REcherchieren: Wie werden Wahrheitswerte in Python ausgedrückt? How are boolean values represented in Python?
#Ü: Sich mit den möglichen Teilfenstern von Pycharm beschäftigen.  Explore the available panes in PyCharm
Höhe = 56.98
print(Höhe)

#du kannst Gleitkommazahlen in eine int konvertieren
F = 78.56
print(F)
print(int(F))
print(F+89)

#use float to add decimal to results
print(float(F+0.44))

#Ü: REcherchieren: Wie werden Wahrheitswerte in Python ausgedrückt? How are boolean values represented in Python?

#Boolean für logical operators_logische operatoren
# #is a comparison operator, represented by True or False symbol. ist ein vergleichsoperator
#<, >, <=, >=, ==, !=, (Größer als, Kleiner als, kleiner gleich, Größer gleich, gleich, ungleich)


age = 60
cancer_age = age > 55 and age < 100
print(cancer_age)

cancer_age = age < 55 or age > 100
print(cancer_age)

cancer_age = age < 55 and age > 100
print(cancer_age)

X = 5
Y = 79
print(X > Y)
print(X < Y)
print(X == Y)

python_score = 80
if python_score >= 80:
    print("you are experienced")
else:
    print("you are a beginner")


