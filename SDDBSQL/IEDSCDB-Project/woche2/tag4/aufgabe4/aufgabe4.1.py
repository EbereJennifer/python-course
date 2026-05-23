
"""
1)
Kleine eigene Klasse mit zwei Attributen, z.B. Person mit vorname und nachname. Klassenvariable anzahl, eine Klassenmethode.

Methoden __init__, __str__, __eq__, __del__

- Mit einigen Objekten ausprobieren
- ein Tupel mit solchen Objekten erzeugen
- ein Dictionary mit Objekten als Values erzeugen.

A simple class with two attributes, e.g., Person with first_name and last_name. A class variable named count, and a class method.

Methods: __init__, __str__, __eq__, __del__

- Experiment with a few objects
- Create a tuple containing such objects
- Create a dictionary with objects as values.
"""
class Person:
    count = 0  # class variable (shared by all objects), Shared across all instances, Tracks how many Person objects exist

    def __init__(self, first_name, last_name): # Runs when object is created, Stores names, Increments count
        self.first_name = first_name
        self.last_name = last_name
        Person.count += 1

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __eq__(self, other):                        # Compares based on content, not memory
        if isinstance(other, Person):
            return (self.first_name == other.first_name and
                    self.last_name == other.last_name)
        return False

    def __del__(self):            # Runs when object is deleted (or garbage collected), Decreases count, Not always predictable when it runs
        Person.count -= 1           # Access class-level data

    @classmethod
    def get_count(cls):
        return cls.count

    # Experiment with objects

p1 = Person("Anna", "Agwaih")
p2 = Person("Ebere", "Chioma")
p3 = Person("Anna", "Sandra")

print(p1)  # Anna Agwaih
print(p1 == p3)  # True
print(Person.get_count())  # 3
#
# # Tuple with objects
#
people_tuple = (p1, p2, p3)
for person in people_tuple:
     print(person)             #Tuples can store objects just like any other data.
#
# # Dictionary with objects as values
people_dict = {
     1: p1,
     2: p2,
     3: p3
 }

print(people_dict[1])