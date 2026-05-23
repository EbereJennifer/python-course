# Anton

#1) Modul konverter.py mit einigen Funktionen für die Umrechnung zwischen verschiedenen Einheiten z.B. Fahrenheit in Celsius, Kilometer in Meilen
# Von konverter_main aus aufrufen


import converter

print("__name__ in converter_main.py ", __name__)

def main():
    km = 13.8
    miles = converter.km_2_mile(km)
    print(f"{km} km sind {miles} miles")

    celsius = 38.9
    fahrenheit = converter.celsius_to_fahrenheit(celsius)
    print(f"{celsius} Grad celsius sind {fahrenheit:.2f} Grad fahrenheit")

if __name__ == "__main__":
    main()