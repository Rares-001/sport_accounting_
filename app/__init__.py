from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config=None):
    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    # Set the database URI before initializing the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/sport_accounting'

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.routes.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    # Fix for 403 error: add the following lines
    CORS(app)

    return app


