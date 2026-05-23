""""
1)
Eine Datenbank wetter.db und eine Tabelle temperaturen mit den Spalten id (autogenerierter primary key), ort, datum, temperatur.

100 zufällige Datensätze erzeugen (z.B. ort aus 10 Städtenamen, temperatur aus Intervall -10.0 - 20.0, datum aus den letzten 100 Tagen) und in Datenbank eintragen.

A database wetter.db and a table temperaturen with the columns id (auto-generated primary key), ort, datum, temperatur.

Generate 100 random records (e.g., ort from 10 city names, temperatur from the range -10.0 - 20.0, datum from the last 100 days)
and insert them into the database.
"""

import sqlite3
import random
from datetime import date, timedelta

connection = sqlite3.connect ("wetter.db")
cursor = connection.cursor()

sql_create = """
            CREATE TABLE IF NOT EXISTS temperaturen (
            nummer INTEGER PRIMARY KEY AUTOINCREMENT,
            ort TEXT,
            datum DATE, 
            temperatur REAL NOT NULL
            )
"""
cursor.execute(sql_create)
connection.commit()


cities = ['Hamburg', 'Berlin', 'Munchen', 'Freiburg', 'Cologne', 'Wurzburg', 'Stuttgart']

for _ in range(100):
    ort = random.choice(cities)

    temperatur = round(random.uniform(-10.0, 20.0), 2)  # .uniform creates random floating numbers and rounds it to 2 decimal places

    past_100_days = random.randint(0, 100)
    datum = date.today() - timedelta(days=past_100_days)


cursor.execute(
        "INSERT  INTO temperaturen (ort, datum, temperatur) VALUES (?, ?, ?)",
    (ort, datum.isoformat(), temperatur))

connection.commit()
connection.close()








