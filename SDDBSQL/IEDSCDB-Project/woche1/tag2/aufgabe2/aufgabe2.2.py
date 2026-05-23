""""
# Define functions, each with SQL parameters if necessary. Pass the parameters as tuples here.

# - show_all
# - delete should delete the record at index nr; read in nr
# - create should create a new record; read in values
# - update should update the record; read in values
#
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
            temperatur REAL
            )
"""
cursor.execute(sql_create)
connection.commit()


def show_all(cursor):
    cursor.execute("SELECT * FROM temperaturen")
    rows = cursor.fetchall()
    for info in rows:
            print(info)

# Deleting a row by its ID (nummer in your table)
def delete(cursor, nr):
    cursor.execute("DELETE FROM temperaturen WHERE nummer = ?", (nr,)) # # (nr,) is a tuple — that’s exactly what the instruction refers to.


def create(cursor, ort, datum, temperatur):
    cursor.execute(
        "INSERT INTO temperaturen (ort, datum, temperatur) VALUES (?, ?, ?)",
        (ort, datum, temperatur)
    )

# To update an already existing row

def update(cursor, nr, ort, datum, temperatur):
    cursor.execute(
        """UPDATE temperaturen 
           SET ort = ?, datum = ?, temperatur = ?
           WHERE nummer = ?""",
        (ort, datum, temperatur, nr)
    )

# to read in values

nr = int(input("Enter ID to delete: "))
delete(cursor, nr)

