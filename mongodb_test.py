import pymongo
from pymongo import MongoClient
Client = MongoClient("mongodb+srv://admin:admin@cluster0.k1mrjrp.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db ["students"]
print(db.list_collection_names) 