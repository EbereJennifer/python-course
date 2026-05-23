# Anton

#1) Modul konverter.py mit einigen Funktionen für die Umrechnung zwischen verschiedenen Einheiten z.B. Fahrenheit in Celsius, Kilometer in Meilen
# Von konverter_main aus aufrufen

print("__name__ in converter.py:", __name__)

def km_2_mile(zahl):
    return 0.6213712 * zahl

def mile_to_km(zahl):
    return zahl / 0.6213712

def celsius_to_fahrenheit(zahl):
    return (zahl * 9 / 5) + 32

def fahrenheit_to_celsius(zahl):
    return (zahl - 32) * 5/9

print(km_2_mile(100))
print(mile_to_km(100))
print(celsius_to_fahrenheit(37))
print(fahrenheit_to_celsius(100))