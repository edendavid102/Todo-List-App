from pymongo import MongoClient

from utils.settings import settings

connection_string = f'mongodb+srv://{settings.user_name}:{settings.password}@cluster0.ihkmf3m.mongodb.net/?retryWrites=true&w=majority'
mongodb_client = MongoClient(connection_string)
print("Connected to the MongoDB database!")

db = mongodb_client[settings.db_name]
