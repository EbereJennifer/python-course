"""
Implement the methods `delete_one_demo` and `delete_many_demo` in MongoHelper and call them from the main program.

2)
Class `Person` with the fields `name` and `location`.
Display the menu in a loop:
Create New Person | Search by Name | Search by Location | Exit

Implement using MongoDB.
"""
from mongo_helper import MongoHelper


def main():
    helper = MongoHelper()
    helper.alles_anzeigen()

    while True:
        befehle = [
            "1 = Neue Person anlegen",
            "2 = Suche nach Name",
            "3 = Suche nach Location",
            "4 = Beenden"
    ]
        info = " | ".join(befehle)
        eingabe = input(info + ": ")
        match eingabe:
            case "1":
                eingabe = input("Eingabe name|ort: ")
                name, ort = result.split("|")
                helper.anlegen(name, ort)
            case  "2":
                eingabe = input("Eingabe name: ")
                helper.suche_name(eingabe.strip())
            case "3":
                eingabe = input("Eingabe ort: ")
                helper.suche_ort(eingabe.strip())
            case "4":
                print(" *** Programm wird beendet *** ")
                break

            case _:
                print("Ungültige Eingabe")

    helper.close()waa

if __name__ == "__main__":
    main()

