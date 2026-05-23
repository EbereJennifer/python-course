# Fallunterscheidung: if, if - else, if - elif -elif -(else)
import random

# Sonderfall: Vergleich auf Gleichheit
# Special case: Comparison of equality

alle = ["Apfel", "Birne", "orange", "Pflaume", "Orange", "salad"]

obst = random.choice(alle)

#if obst == "Apfel":
match obst:
    case "Apfel":
        print("Apfel gewählt")
    case "Birne":
        print("Birne gewählt")
    case "orange":
        print("Orange gewählt")
    case "Pflaume":
        print("Pflaume gewählt")
    case _:
        print("Unbekannt")

"""
match looks at the value of obst
- It compares it against each case in order
- If a case matches, its block runs
_ is a wildcard / default case (like else)

match does not “call” a function — it’s a control-flow statement
Python 3.10+ only
_ = default case
Case-sensitive!

🔹 Why use match instead of if/elif
Cleaner and easier to read when you have many discrete options
Can do more advanced pattern matching in Python 3.10+

"""