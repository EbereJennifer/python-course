
from pymongo import MongoClient
client = MongoClient()
db = client.bank_db
coll = db.konten

class MongoHelper:
    def insert_one_demo(self, konto):
        result = coll.insert_one(konto)
        print(f"inserted id: {result.inserted_id}")

    def insert_many_demo(self, konten):
        result = coll.insert_many(konten)
        print(f"inserted ids: {result.inserted_ids}")

    def find_one_demo(self, filter={}):
        result = coll.find_one(filter)
        print(result)

    def find_demo(self, filter={}):
        cursor = coll.find(filter)
        for i, doc in enumerate(cursor, start=1):
            print(f"{i}. {doc}")
        print()

    def update_one_demo(self, filter, update_doc):
        result = coll.update_one(filter, update_doc)
        print(f"count updated: {result.modified_count}")

    def update_many_demo(self, filter, update_doc):
        result = coll.update_many(filter, update_doc)
        print(f"count updated: {result.modified_count}")

    def delete_one_demo(self, filter):
        result = coll.delete_one(filter)
        # print(f"count deleted: {result.deleted_count}")


mongo_helper = MongoHelper()
def main():
    konto = {"inhaber": "Elam Oussoni", "kontostand": 23.99}
    #mongo_helper.insert_one_demo(konto)

    # Ü: insert_many_demo mit Liste von mind. 3 Konten
    konten = [
        {"inhaber": "Elisabeta Romanczyk", "kontostand": -10.0},
        {"inhaber": "Timo Benscher", "kontostand": 120.0},
        {"inhaber": "Yana Odreana", "kontostand": 44.87}
     ]
    #mongo_helper.insert_many_demo(konten)
    filter = { "inhaber": "Timo Benscher" }
    #mongo_helper.find_one_demo(filter)
    mongo_helper.update_one_demo({}, {"$inc": {"kontostand": 100}})
    mongo_helper.find_demo()
    #filter = {"kontostand": {"$lt": 50}}
    update_doc = {"$inc": {"kontostand": 0.99}}
    # mongo_helper.find_demo(filter)
    # mongo_helper.update_many_demo(filter, update_doc)
    # mongo_helper.find_demo(filter)

    #filter = {"inhaber": {"$eq": "Elam Oussoni"}}
    #Smongo_helper.find_demo(filter)
    #mongo_helper.delete_one_demo(filter)
    #print("Alle:")
    #mongo_helper.find_demo()

    konten = [
        {"inhaber": "Meier", "kontostand": 12.37},
        {"inhaber": "Meier", "kontostand": 78.17},
        {"inhaber": "Meier", "kontostand": 67.24},
        {"inhaber": "Meier", "kontostand": 34.89}
    ]

    # mongo_helper.insert_many_demo(konten)
    mongo_helper.find_demo()

    filter = {"inhaber": "Maier"}
    mongo_helper.delete_many_demo(filter)
    print("*" * 40)
    mongo_helper.find_demo()

if __name__ == "__main__":
    main()






