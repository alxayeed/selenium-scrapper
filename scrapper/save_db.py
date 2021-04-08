import pymongo
import json

client = pymongo.MongoClient(
    'mongodb+srv://alroot:alroot000@cluster0.hvo9b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')


# database
db = client["GFG"]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["data"]

# Loading or Opening the json file
with open('comments.json') as file:
    file_data = json.load(file)

# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)
