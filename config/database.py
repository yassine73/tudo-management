from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://admin:admin123@cluster0.s0bmy8a.mongodb.net/?appName=Cluster0")

db = client.todo_db

collection_name = db["todo_collection"]