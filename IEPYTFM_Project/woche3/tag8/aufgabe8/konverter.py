# 1) Modul konverter.py mit einigen Funktionen für die Umrechnung zwischen verschiedenen Einheiten
# z.B. Fahrenheit in Celsius, Kilometer in Meilen Von konverter_main aus aufrufen
from string.templatelib import convert


def convert_units(value, unit):
    if unit == "f":   # Fahrenheit
        result = (value - 32) * 5 / 9
        print(f"{result} Celsius")
    elif unit == "c":
        result = (value * 9 / 5) + 32
        print(f"{result} fahrenheit")
    elif unit == "m":
        result = (value / 1000)
        print(f"{result} Kilometers")
    elif unit == "kg":
        result = (value * 1000)
        print(f"{result} grams")
    else:
        print(f"Invalid unit", unit)

print(convert_units(56, "f"))
print(convert_units(40, "c"))
print(convert_units(6774, "kg"))
print(convert_units(20000, "m"))
