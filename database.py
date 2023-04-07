from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient

db = SQLAlchemy()

MONGO_CONNECTION_STRING = "mongodb+srv://Rares:admin@cluster0.y9osbya.mongodb.net/MT940_id?retryWrites=true&w=majority"


mongo_client = MongoClient(MONGO_CONNECTION_STRING)

mongo_db = mongo_client.get_database('MT940_id')

user_collection = mongo_db['user_collection']
