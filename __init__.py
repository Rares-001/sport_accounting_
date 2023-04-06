from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"] = "c004fab132cf54330558d4fa00d5309f058f9c60"
app.config["MONGO_URI"] = "mongodb+srv://Terry:PA$$W0RD@cluster0.y9osbya.mongodb.net/?retryWrites=true&w=majority"

#setup of mongodb
mongodb_client = MongoClient(app)
db = mongodb_client

