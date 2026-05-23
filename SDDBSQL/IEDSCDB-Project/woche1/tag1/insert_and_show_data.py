import sqlite3
import random

def create_table():
    connection = sqlite3.connect("neuer_verein.db")
    cursor = connection.cursor()
    sql_create = """
                 CREATE TABLE IF NOT EXISTS mitglieder 
                 (
                     nummer INTEGER PRIMARY KEY,
                     vorname TEXT, 
                     nachname TEXT, 
                     geburtstag TEXT, 
                     betrag REAL
                 ) 
                 """
    cursor.execute(sql_create)
    connection.close()


def insert_example():
    connection = sqlite3.connect("neuer_verein.db")
    cursor = connection.cursor()
    zufall = random.randint(100000, 1000000)
    sql = f"INSERT INTO mitglieder VALUES({zufall}, 'Julia', 'Todorovic', '27.9.2001', 49.99)"

    cursor.execute(sql)
    connection.commit()
    connection.close()


def show_all_data():
    connection = sqlite3.connect("neuer_verein.db")
    cursor = connection.cursor()

    sql_select = "SELECT * FROM mitglieder"

    cursor.execute(sql_select)

    for spalte in ["Nummer", "Vorname", "Nachname", "Geburtstag", "Beitrag"]:
        print(f"{spalte:>15}", end="")

    print()
    print("*" * 75)

    for datensatz in cursor:
        for item in datensatz:
            print(f"{item:>15}", end="")
        print()

    connection.close()


create_table()
insert_example()
show_all_data()
