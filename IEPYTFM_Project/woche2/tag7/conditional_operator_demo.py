# Möglich als Abkürzung für if - else
# wenn in beiden Fällen eine Variable
# einen wert erhält
# Possible as an abbreviation for if - else
# when in both cases a variable
# receives a value

n = 44

text = "gerade" if n % 2 == 0 else "ungerade"

print(n, text)

liste_zahlen = [2, 7, 5, 8, 3]
ergebnis = ["gerade" if zahl % 2 == 0 else "ungerade" for zahl in liste_zahlen]
print(ergebnis)