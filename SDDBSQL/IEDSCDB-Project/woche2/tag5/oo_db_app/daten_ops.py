import sqlite3

class DatenHelper:
    def __init__ (self, db_pfad):
        self.db_pfad = db_pfad
        self.connection = sqlite3.connect(db_pfad)
        self.cursor = self.connection.cursor()

    def tabelle_erstellen(self):
        #DDL: keine SQL Parameter
        sql = """
            CREATE TABLE IF NOT EXISTS kunden (
        nummer INTEGER PRIMARY KEY,
        name, TEXT NOT NULL,
        email TEXT NOT NULL
        )
        """
        self.cursor.execute(sql)
        self.connection.commit()

    def alle_daten(self):
        sql = "SELECT * FROM kunden"
        self.cursor.execute(sql)
        # commit nicht nötig bei lesemethoden
        return self.cursor.fetchall()
        #print(type(ergebnis), ergebnis)


    def alle_anzeigen(self):
        print(f"{'Nummer':10}", end="")
        print(f"{'Name':>20}", end="")
        print(f"{'Email':>20}")
        print("*" * 50)
        ergebnis = self.alle_daten()

        for datensatz in ergebnis:
            print(f"{datensatz[0]:10}", end="")
            print(f"{datensatz[1]:>20}", end="")
            print(f"{datensatz[2]:>20}")

        def verbindung_beenden(self):
            self.connection.close()



# Außerhalb der klasse
def main():
    helper = DatenHelper("kunde.db")
    helper.tabelle_erstellen()
    ergebnis = helper.alle_daten()
    helper.alle

if __name__ == "__main__":
    main()


