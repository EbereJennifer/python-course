

import sqlite3

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

eingabe = input("Tabellenname: ")
sql = """
    CREATE TABLE IF NOT EXISTS ? (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        zusatz TEXT
    )
"""

# cursor.execute(sql, [eingabe.strip()])  SQL-Parameter nicht erlaubt
# cursor.execute(sql)  Ungültiges SQL

cursor.commit()
conn.close()

#Parameter in f-string möglich
print(f"Eingabe war: {eingabe}")

# Auch möglich: SQL so zusammensetzen:
# kein SQL-Parameter, SQL-Injektion weiter möglich
Bad_sql_string = """
    CREATE TABLE IF NOT EXISTS {eingabe} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        zusatz TEXT
    )
"""

