import sqlite3

conn = sqlite3.connect("personal")
cursor = conn.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS memos (
        nr INTEGER PRIMARY KEY AUTOINCREMENT,
        titel TEXT NOT NULL,
        zusatz TEXT,
        zeit TEXT
    )
"""

cursor.execute(sql)
conn.commit()

def anzeigen():
    sql_select = "SELECT * FROM memos"
    cursor.execute(sql_select)
    for spalte in ["nr", "titel", "zusatz", "zeit"]:
        print(f"{spalte:>15}", end="")
    print()
    print("*" * 60)
    for datensatz in cursor:
        for item in datensatz:
            if item is None:
                item = "-"
            print(f"{item:>15}", end="")
        print()

sql = "INSERT INTO memos VALUES(NULL, 'AB getroffen', 'Geld geliehen', NULL)"
cursor.execute(sql)
conn.commit()

# Zur Vermeidung von SQL Injection:
# Benutzereingabe nur als Parameter in SQL-Befehle einsetzen
# nicht in normale Python Strings einsetzen
# geht in CRUD Befehlen: CREATE - READ - UPDATE - DELETE

gesamt = input("Eingabe: titel|zusatz|zeit: ")
titel, zusatz, zeit = gesamt.split("|")
sql = "INSERT INTO memos (titel, zusatz, zeit) VALUES (?, ?, ?)"
cursor.execute(sql, (titel, zusatz, zeit))
conn.commit()

anzeigen()

result = input("Nr. zum Löschen (oder leer): ")
if result != "":
    nr = int(result)
    sql = "DELETE FROM memos WHERE nr = ?"
    cursor.execute(sql, (nr,))
    conn.commit()

print()
anzeigen()

conn.close()















