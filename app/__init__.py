from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from config import Config

# initialize the Flask application
app = Flask(__name__)

# load the app configuration from the Config class
app.config.from_object(Config)

# initialize the MongoDB database
mongo = MongoEngine(app)

# initialize the Postgres database
db = SQLAlchemy(app)

# import the routes module to register the routes with the app
from app import routes
