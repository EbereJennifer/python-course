from pymongo import MongoClient

class MongoHelper:
    def __init__(self):
        client = MongoClient()
        self.collection = self.client.my_db.personen

    def close(self):
        self.client.close()

    def anlegen(self, name, ort):
        result = self.collection.insert_one({"name": name, "ort": ort})
        print("Angelegt:", result.inserted_id)

    # def alles_anzeigen(self):
    #     cursor = self.collection.find({})
    #     for i, elem in enumerate(cursor, start=1):
    #         print(f"{i}, {elem}")
    #     print("*" * 40)

    def alles_anzeigen(self):
        cursor = self.collection.find({})
        self.show_content(cursor)

    def show_content(self, cursor):
        for i, elem in enumerate(cursor, start=1):
            print(f"{i}. {elem}")
        print("*" * 40)

    def suche_name(self, name):
        cursor = self.collection.find({"Eingabe name": name})
        self.show_content(cursor)

    # def suche_ort(self, ort):
    #     cursor = self.collection.find({"Eingabe ort": ort})
    #     helper.suche_ort(eingabe.strip())
    #     self.show_content(cursor)

def main():
    helper = MongoHelper()
    helper.anlegen("Kyungo", "Mannheim")
    helper.alles_anzeigen()



