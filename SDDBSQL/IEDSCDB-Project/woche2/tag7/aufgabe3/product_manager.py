"""
3)
Work with either SQLite or PostgreSQL (research required here).

The ProductManager class uses the waren_db database:
Products table with number, name, manufacturer_id, is_eol,
Manufacturers table with manufacturer_id, name, location.
Establish appropriate foreign key relationships between the two tables.

Test SQL operations (INSERT, SELECT, UPDATE, DELETE) and define appropriate methods for them. Also include methods to display all products from a specific manufacturer.

Enter JetBrains IDE products as sample data.

PRAGMA foreign_keys = ON;

"""

import sqlite3
conn = sqlite3.connect('waren.db')
cursor = conn.cursor()
conn.execute("PRAGMA FOREIGN_KEYS = ON;")

class ProduktManager:
    def create_tables(self):
        sql = """
            CREATE TABLE IF NOT EXISTS hersteller(
                hersteller_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                ort TEXT
            );
        """
        cursor.execute(sql)

        sql = """
        CREATE TABLE IF NOT EXISTS produkte(
            nummer INTEGER PRIMARY KEY,
            name TEXT,
            hersteller_id INTEGER,
            is_eol INTEGER,
            FOREIGN KEY (hersteller_id) REFERENCES hersteller(hersteller_id)
            );
        """
        cursor.execute(sql)

    def insert_data(self):
        sql = "INSERT INTO hersteller (name, ort) VALUES ('Jetbrains', 'Prag');"
        cursor.execute(sql)
        conn.commit()

        sql = "INSERT INTO hersteller (name, ort) VALUES ('Apple', 'Cupertino');"
        cursor.execute(sql)
        conn.commit()
        sql = "INSERT INTO produkte VALUES (?, ?, ?, ?)"
        daten = [
            (1567, "Pycharm", 1, 0),
            (6748, "Intellij", 1, 0),
            (2657, "Rider", 1, 0),
            (7865, "GoLand", 1, 0),
            (9876, "Rider", 2, 1),

            (64547, "ipod", 2, 1),
            (63536, "MacBook Air", 2, 0),
            (72635, "Mac Mini", 2, 1)
        ]
        for tupel in daten:
            cursor.execute(sql, tupel)
            conn.commit()

    def show_data(self):
        sql = """
            SELECT produkte.name, hersteller.name
            FROM produkte JOIN hersteller
            ON produkte.hersteller_id = hersteller.hersteller_id;"""
        cursor.execute(sql)
        for rows in cursor:
            print(rows)

    def show_produkte(self, hersteller_pk):
        sql = " SELECT nummer, name, is_eol FROM produkte WHERE hersteller_id = ?"
        cursor.execute(sql, (hersteller_pk,))
        for rows in cursor:
            print(rows)

    def update_produkt(self, pk, neuer_name):
        sql = "UPDATE produkte SET name=? WHERE nummer=?"
        cursor.execute(sql, [neuer_name, pk])
        conn.commit()

    def delete_produkt(self, nummer):
        sql = "DELETE FROM produkte WHERE nummer = ?"
        cursor.execute(sql, [nummer])

manager = ProduktManager()
#manager.create_tables()
#manager.insert_data()
#manager.show_data()
#manager.show_produkte(1)
#manager.update_produkt(83644, "CLion")
#manager.show_produkte(1)
#manager.delete_produkt(1576)
manager.show_produkte(1)
#cursor.execute("DELETE FROM hersteller WHERE hersteller_id = 1") # verboten
conn.commit()
conn.close()

