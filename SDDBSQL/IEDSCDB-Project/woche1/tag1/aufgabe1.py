# 1)
# library.py script:
# Create a database named library.db
# and a table named books with the columns “isbn” (primary key), “author”, ‘title’, and “year”.
#
# Functions:
# - show_all should display all data clearly
# - input_book should allow values for isbn, author, title, and year to be entered and insert them into the database as a new record.
#
# - Main program: Menu with 3 options—Display, Enter, Exit—as a loop.




import sqlite3


def create_booktable():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    create_booktable = """
                CREATE TABLE IF NOT EXISTS books
                (
                    isbn INTEGER PRIMARY KEY,
                    author TEXT,
                    title TEXT,
                    year INTEGER
                )
                """
    cursor.execute(create_booktable)
    connection.close()



# If you want to skip duplicates: to prevent integrity error
#
# cursor.execute(
#     "INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?)",
#     values
# )

def input_book():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    values = (40, 'Ebere', 'The rising of the Sun', 2026)
    cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)", values)

    connection.commit()
    connection.close()


import sqlite3


def show_all_data():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    show_all = "SELECT * FROM books"
    cursor.execute(show_all)

    for columns in ["isbn", "autor", "titel", "jahr"]:

        print(f"{columns:>15}", end="")

        # rows
    for row in cursor.fetchall():
        for value in row:
            print(f"{value:>15}", end="")
        print()

    connection.close()

def main():
    create_booktable()  # make sure table exists

    while True:
        print("\n--- Menü ---")
        print("1: Anzeigen")
        print("2: Eingeben")
        print("3: Beenden")

        choice = input("Bitte wählen: ")

        if choice == "1":
            show_all_data()

        elif choice == "2":
            input_book()

        elif choice == "3":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe!")

main()