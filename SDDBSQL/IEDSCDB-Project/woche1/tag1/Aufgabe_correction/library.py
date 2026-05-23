
import sys
import sqlite3


def init():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    sql = """
          CREATE TABLE IF NOT EXISTS books 
          ( 
              isbn  TEXT PRIMARY KEY, 
              autor TEXT    NOT NULL, 
              titel TEXT    NOT NULL, 
              jahr  INTEGER NOT NULL 
          ) 
          """
    cursor.execute(sql)
    conn.commit()
    conn.close()


def anzeigen():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    sql_select = "SELECT * FROM books"
    cursor.execute(sql_select)
    for spalte in ["isbn", "autor", "titel", "jahr"]:
        print(f"{spalte:>15}", end="")
    print()
    print("*" * 60)
    for datensatz in cursor:
        for item in datensatz:
            print(f"{item:>15}", end="")
        print()
    connection.close()


def eingeben():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    eingabe = input("Datensatz isbn, autor, titel, jahr: ")

    try:
        parts = [p.strip() for p in eingabe.split(",")]

        if len(parts) != 4:  # parts is a list created from the input: len(parts) = 4 (because there are 4 items)
            print("Bitte genau 4 Werte eingeben!")
            return

        isbn, autor, titel, jahr = parts

        cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?)",
            (isbn, autor, titel, int(jahr))
        )

        conn.commit()
        print("Datensatz gespeichert.")

    except ValueError:
        print("Jahr muss eine Zahl sein!")
    except sqlite3.IntegrityError:       # What is an IntegrityError? It’s an error raised by SQLite when you violate a rule in the database.
                                            # In your table: isbn TEXT PRIMARY KEY, This means: Every isbn must be unique You cannot insert the same isbn twice
        print("ISBN existiert bereits!")
    finally:
        conn.close()




    # input_isbn, input_autor, input_titel, input_jahr = eingabe.split(", ")
    #
    # sql = f"""
    #     INSERT INTO books VALUES ('{input_isbn}', '{input_autor}', '{input_titel}', '{input_jahr}')
    # """
    #
    # cursor.execute(sql)
    # conn.commit()
    # conn.close()









def main():
    #init()

    while True:
        
        befehl = input("Anzeigen - Eingeben - Beenden: ")
        match befehl.strip().lower():
            case "anzeigen":
                anzeigen()
                print()
            case "eingeben":
                eingeben()
                print()
            case "beenden":
                sys.exit(0)  # Programm ordnungsgemäß beenden
            case _:
                pass


if __name__ == "__main__":
    main()

#
# What it does:
# match checks a value (command)
# case defines possible matches
# _ is a default case (like else)
# Equivalent using if:
# cmd = command.strip().lower()
#
# if cmd == "show":
#     show()
# elif cmd == "enter":
#     enter()
# elif cmd == "exit":
#     sys.exit(0)
# else:
#     pass