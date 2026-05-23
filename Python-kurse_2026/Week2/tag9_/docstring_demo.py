# A docstring (short for documentation string) is a special string in Python used to describe what your code does.
# It’s like a built-in comment that tools and other programmers can read easily.
#
#  What is a docstring?
#
# A docstring is written using triple quotes (""" ... """) and placed:
#
# right after a function
# right after a class
# or at the top of a file






# docstring wird als erstes im Rumpf einer Funktion notiert

def berechne_quadrat(n):     # calculate_square
    """
    gibt das quadrat einer Zahl züruck.
    
    Arguments:
        n(int oder float): inputwert
        
    Rückgabe:
        Quadrat von n
    ********************************************************
    Returns the square of a number.
    
    Arguments:
        n (int or float): input value
        
    Return value:
        The square of n
        
    """
    return n * n
result = berechne_quadrat(13)
print(result)
#print(berechne_quadrat.__doc__)
help(berechne_quadrat)


liste_zahlen = [2, 8, 17, 23]
# ü liste_quadratzahlen mit map-Funktion
result = map(berechne_quadrat, liste_zahlen)
liste_quadratzahlen = list(result)
print(liste_quadratzahlen)

# Andere Art: List comprehension
result_list = [ element for element in liste_zahlen] #this makes the new list the same as the old list
print(result_list)

# Andere Art: List comprehension
result_list = [ element + 1 for element in liste_zahlen] #this makes the new list the same as the old list
print(result_list)

# Andere Art: List comprehension
# python hat einige Elemente funktionaler Programmiersprachen
# (Haskell, Lisp, Scala)
# übernommen, etwas Comprehensions für List, set, Dictionary
result_list = [ berechne_quadrat(element) for element in liste_zahlen] #this makes the new list the same as the old list
print(result_list)



