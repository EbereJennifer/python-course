import sqlite3
import random
import datetime

conn = sqlite3.connect("wetter.db")  # DB wird generiert, falls nötig
cursor = conn.cursor()
cities = ["Berlin", "Bonn", "Köln", "Hamburg", "Nuremberg", "Munich", "Dresden", "Regensburg", "Mannheim", "Dortmund"]
sql = """
    CREATE TABLE IF NOT EXISTS temperaturen 
    ( 
    id         INTEGER PRIMARY KEY AUTOINCREMENT, 
    ort        TEXT NOT NULL, 
    datum      TEXT NOT NULL, 
    temperatur REAL NOT NULL
) 
"""
cursor.execute(sql)
conn.commit()

def create_row(ort, datum, temperatur):
    sql = """
        INSERT INTO temperaturen (ort, datum, temperatur) 
        VALUES (?, ?, ?); 
    """
    cursor.execute(sql, (ort, datum, temperatur))
    conn.commit()

def show_all():
    sql = """
        SELECT * FROM temperaturen 
    """
    cursor.execute(sql)
    conn.commit()  # optional
    print()
    print("*" * 48)
    for title in ["id", "ort", "datum", "temperatur"]:
        print(f"{title:>12}", end="")
    print()
    print("_" * 48)
    for row in cursor:
        for item in row:
            print(f"{item:>12}")
    print("*" * 48)
    print()


def delete():
    eingabe = input("nr für Datensatz zum Löschen: ")
    try:
        nr = int(eingabe)
        sql = "DELETE FROM temperaturen WHERE id = ?"
        cursor.execute(sql, (nr,))
        conn.commit()
    except ValueError:
        print("Keine gültige Eingabe")


for _ in range(1):
    ort = random.choice(cities)
    delta = datetime.timedelta(days=random.randint(1, 100))
    datum = datetime.date.today() - delta
    temperatur = random.uniform(-10.0, 20.0)
    create_row(ort, datum.isoformat(), temperatur)

show_all()
delete()
show_all()
conn.close()
