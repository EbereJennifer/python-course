# Konvention in Python für Hauptfunktion, ist keine pflicht
# Funktion "main" soll nur ausgeführt werden,
# wenn __name__den Wert "__main"__ hat
# Convention in Python for the main function, is not mandatory
# Function "main" should only be executed
# if __name__ has the value "__main__"


# wird nicht ausgeführt, falls main_demo importiert wird
def main():
    print("Hauptprogramm")

if __name__ == "__main__":
    main()

print(f"Wert von __name__ in main_demo-py: {__name__}")

