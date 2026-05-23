import calculate

c = calculate.add(3, 7)
print(c)

d = calculate.subtract(10, 6)
print(d)
print("**********************************************************")


import sys # for system

sys.path.append("zusatzmodule") # dort werden jetzt Module gesucht import zusatzmodule.zusatzoperationen
import zusatzmodule.zusatzoperationen

erg = zusatzmodule.zusatzoperationen.euler(4.5678)
print(erg)

from zusatzmodule.zusatzoperationen import euler
print(euler(9.123))