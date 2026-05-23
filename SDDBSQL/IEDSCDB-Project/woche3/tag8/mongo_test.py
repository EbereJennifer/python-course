from pymongo import MongoClient
# This is the connection string (URI).
# localhost means the database is running on your own machine.
# 27017 is the default port for MongoDB.
# ⚠️ Note: In your code, this variable is defined but not actually used later.

uri = "mongodb://localhost:27017/"
client = MongoClient()              # This creates a connection to MongoDB. Since no URI is passed, it defaults to mongodb://localhost:27017/.
                                    # So effectively, it connects to your local MongoDB server.

db = client.test_db # noch nicht erzeugt  # This accesses a database named test_db. The comment (“noch nicht erzeugt” = “not yet created”) is correct.
                                                                 # MongoDB creates the database automatically when you first store data in it.
collection = db.test_collection   # This accesses a collection (like a table in SQL) called test_collection. Again, it doesn’t physically exist yet — it will be created on first insert.
collection.insert_one({"name": "Max Mustermann", "alter": 28, "rolle": "Tester"})  # This inserts one document (similar to a row in SQL).The document is a Python dictionary.
                                                                                    # MongoDB automatically adds an _id field (unique identifier).
                                                                                        # After this line:
                                                                                        # test_db database is created
                                                                                        # test_collection collection is created
                                                                                        # The document is stored

print(client.list_database_names())
result = collection.find_one({})#“Give me one document”
                                #{} is an empty filter → matches everything
                                    # So it returns the first document it finds in the collection.
print(result)




# Ü: Weiteres Dokument einfügen und wieder finden und anzeigen lassen. Insert another document, then locate and display it


result = collection.insert_many(
    [{"name": "Anton Kölbl", "alter": 30, "rolle": "Intern"},
    {"name": "Diana Alhadad", "alter": 23, "rolle": "Entwickler"},
    {"name": "Oliver Armbruster", "alter": 25, "rolle": "Admin"},
    {"name": "Tahir Elamin", "alter": 20, "rolle": "Tester"}
])
print(result.inserted_ids)
print(type(result))

#Anton
# Ü: Weiteres Dokument einfügen und wieder finden und anzeigen lassen. Insert another document, then locate and display it

#collection.insert_one({"_id": 12345, "vorname": "Eno", "beruf": "Entwickler"})
filter = {"vorname": "Eno"}
result = collection. find_one (filter)

for key, valve in result.items():
    print(f"{key}: {value}", end="")
print()
collection.insert_one({"_id": "Das soll eine4 id sein", "sprache": "DE"})

print(collection.find_one({"sprache": "DE"}))