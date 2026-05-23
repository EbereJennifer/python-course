




import sqlite3

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


# Strg+Leer
conn = sqlite3.connect("personal")
cursor = conn.cursor()
anzeigen()
print()
result = input("Löschen Nr. (oder leer): ")
if result.isdigit():
    zahl = int(result)
    sql = "DELETE FROM memos WHERE nr = :param_nr"
    cursor.execute(sql, { "param_nr": zahl })
    conn.commit()

print()
anzeigen()


# Ü: Input: Updaten für nr: titel, zusatz, zeit
# SQL Update durchführen mit 4 Parameter bevorzugt als Dictionary
# Beispiel UPDATE memos SET zusatz = 'vielleicht', zeit = 'Morgen' WHERE nr = 12

result = input("Update? nr|titel|zusatz|zeit: ")
nr, titel, zusatz, zeit = result.split("|")
sql = """UPDATE memos SET 
                          titel = :param_titel, 
                          zusatz = :param_zusatz, 
                          zeit = :param_zeit 
         WHERE nr=:param_nr"""
cursor.execute(sql, {
    "param_titel": titel,
    "param_zusatz": zusatz,
    "param_zeit": zeit,
    "param_nr": nr}
)
conn.commit()

anzeigen()

conn.close()














